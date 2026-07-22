from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import UserSignupForm, AssociateProfileForm  # Updated import

def home_view(request):
    return render(request, 'accounts/base.html')

def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            auth_login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials or not an admin.')
    return render(request, 'accounts/admin_login.html')

def associate_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.user_type == 'associate':
            auth_login(request, user)
            return redirect('associate_dashboard')  # Redirect to associate dashboard
        else:
            messages.error(request, 'Invalid credentials or not an associate.')
    return render(request, 'accounts/associate_login.html')

def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after password reset
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/reset_password.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            auth_login(request, user)  # Log the user in
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserSignupForm()  # Render an empty form for GET requests

    return render(request, 'accounts/signup.html', {'form': form})