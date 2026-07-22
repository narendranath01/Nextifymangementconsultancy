# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser , AssociateProfile
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, validate_integer
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=17, required=True)
    business_name = forms.CharField(max_length=100, required=True)
    official_email = forms.EmailField(required=True)
    deals_in = forms.CharField(max_length=100, required=True)
    establishment_year = forms.IntegerField(required=True)
    connecting_person = forms.CharField(max_length=100, required=True)
    connecting_person_contact = forms.CharField(max_length=17, required=True)
    user_type = forms.ChoiceField(choices=[('user', 'User')], required=True)  # Add user_type field

    class Meta:
        model = CustomUser  # Use CustomUser instead of User
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'business_name', 'official_email', 'deals_in', 'establishment_year', 'connecting_person', 'connecting_person_contact', 'user_type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove 'associate' and 'admin' from the user_type choices
        self.fields['user_type'].choices = [choice for choice in self.fields['user_type'].choices if choice[0] not in ['associate', 'admin']]

 


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    )
 
# accounts/forms.py


class AssociateProfileForm(forms.ModelForm):
    class Meta:
        model = AssociateProfile
        fields = ('user', 'department', 'role', 'joining_date')