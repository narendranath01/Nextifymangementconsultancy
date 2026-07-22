from django.db import models
from django.contrib.auth.models import AbstractUser

class Associate(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_age = models.IntegerField()
    phone_no = models.CharField(max_length=15)
    adhar_no = models.CharField(max_length=12)
    pan_no = models.CharField(max_length=10)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class User(AbstractUser):
    business_email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    business_name = models.CharField(max_length=100, blank=True, null=True)
    official_email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    deals_in = models.CharField(max_length=100, blank=True, null=True)
    establishment_year = models.PositiveIntegerField(blank=True, null=True)
    connecting_person = models.CharField(max_length=100, blank=True, null=True)
    connecting_person_contact = models.CharField(max_length=15, blank=True, null=True)

    # Additional fields can be added as needed

class ServiceRendered(models.Model):
    business_name = models.CharField(max_length=100)
    turnover = models.DecimalField(max_digits=10, decimal_places=2)
    service_type = models.CharField(max_length=100)
    details = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
