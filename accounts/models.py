from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver

# Constants for user types
USER_TYPE_CHOICES = [
    ('user', 'User'),
    ('associate', 'Associate'),
    ('admin', 'Admin'),
]

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    business_name = models.CharField(max_length=100, blank=True)
    official_email = models.EmailField(blank=True)
    deals_in = models.CharField(max_length=100, blank=True)
    establishment_year = models.IntegerField(null=True, blank=True)
    connecting_person = models.CharField(max_length=100, blank=True)
    connecting_person_contact = models.CharField(max_length=17, blank=True)

    # Fix for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_groups",  # Unique related_name
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions",  # Unique related_name
        related_query_name="customuser",
    )

    def __str__(self):
        return self.username

    # Custom validation for establishment_year
    def clean(self):
        if self.establishment_year and self.establishment_year < 1900:
            raise ValidationError({'establishment_year': 'Establishment year must be after 1900.'})

    # Ensure user_type cannot be changed after creation
    def save(self, *args, **kwargs):
        if self.pk:
            original = CustomUser.objects.get(pk=self.pk)
            if original.user_type != self.user_type:
                raise ValidationError({'user_type': 'User type cannot be changed after creation.'})
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.TextField(blank=True, help_text="A short bio about the user.")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, help_text="Profile picture of the user.")
    date_of_birth = models.DateField(null=True, blank=True, help_text="User's date of birth.")
    address = models.CharField(max_length=255, blank=True, help_text="User's address.")

    def __str__(self):
        return f"{self.user.username}'s Profile"


class AssociateProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='associate_profile')
    department = models.CharField(max_length=100, blank=True, help_text="Department the associate belongs to.")
    role = models.CharField(max_length=100, blank=True, help_text="Role of the associate in the organization.")
    joining_date = models.DateField(null=True, blank=True, help_text="Date the associate joined the organization.")

    def __str__(self):
        return f"{self.user.username}'s Associate Profile"


class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='admin_profile')
    admin_level = models.CharField(max_length=50, blank=True, help_text="Level of admin access (e.g., Super Admin, Moderator).")
    access_areas = models.TextField(blank=True, help_text="Areas the admin has access to.")

    def __str__(self):
        return f"{self.user.username}'s Admin Profile"


# Django Signals to automatically create profiles when a user is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'user':
            UserProfile.objects.create(user=instance)
        elif instance.user_type == 'associate':
            AssociateProfile.objects.create(user=instance)
        elif instance.user_type == 'admin':
            AdminProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'user':
        instance.user_profile.save()
    elif instance.user_type == 'associate':
        instance.associate_profile.save()
    elif instance.user_type == 'admin':
        instance.admin_profile.save()