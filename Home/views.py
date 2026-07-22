from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import Blog  # Importing the Blog model


def home(request):
    blogs = Blog.objects.all().order_by('-date_posted')[:6]  # Fetch the latest 6 blogs
    return render(request, 'Home/Home.html', {'blogs': blogs})

# Blog-related views
def blog_list(request):
    blogs = Blog.objects.all().order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

# Static page views
# Home Page
def home(request):
    return render(request, 'Home/Home.html')

# About Page
def about(request):
    return render(request, 'Home/About.html')

# Services Pages
def business_analytics(request):
    return render(request, 'Home/businessanalytics.html')

def finance_analytics(request):
    return render(request, 'Home/financeanalytics.html')

def market_analytics(request):
    return render(request, 'Home/marketanalytics.html')

def market_research(request):
    return render(request, 'Home/MarketResearch.html')

def seo(request):
    return render(request, 'Home/Seo.html')

def management_consulting(request):
    return render(request, 'Home/managementconsulting.html')

def organizational_development(request):
    return render(request, 'Home/orgdevelopment.html')

def risk_management(request):
    return render(request, 'Home/RiskManagement.html')

def strategic_planning(request):
    return render(request, 'Home/StrategicPlanning.html')

def change_management(request):
    return render(request, 'Home/ChangeManagement.html')

def other_services(request):
    return render(request, 'Home/others.html')

def finance(request):
    return render(request, 'Home/finance.html')

def strategic_planning(request):
    return render(request, 'Home/StrategicPlanning.html')

# Contact Page
def contact_us(request):
    return render(request, 'Home/ContactUs.html')

# Authentication views
def signup_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Validation
        if get_user_model().objects.filter(email=email).exists():
            error_message = _("Email already exists.")
        else:
            # Create user
            user = get_user_model().objects.create_user(username=username, email=email, password=password)

            # Save additional fields
            user.business_name = request.POST.get('business_name', '')
            user.official_email = request.POST.get('official_email', '')
            user.contact_number = request.POST.get('contact_number', '')
            user.deals_in = request.POST.get('deals_in', '')
            user.establishment_year = request.POST.get('establishment_year', '')
            user.connecting_person = request.POST.get('connecting_person', '')
            user.connecting_person_contact = request.POST.get('connecting_person_contact', '')
            user.save()

            return redirect('login')

    return render(request, 'accounts/signup.html', {'error_message': error_message})

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.user_type == 'user':
                return redirect('home')
            elif user.user_type == 'associate':
                return redirect('blog_list')
            elif user.user_type == 'admin':
                return redirect('admin_dashboard')
        else:
            error_message = "Invalid username or password."

    return render(request, 'accounts/login.html', {'error_message': error_message})

def associate_login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.user_type == 'associate':
            login(request, user)
            return redirect('blog_list')
        else:
            error_message = "Invalid username or password."

    return render(request, 'accounts/associate_login.html', {'error_message': error_message})

def admin_login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.user_type == 'admin':
            login(request, user)
            return redirect('admin_dashboard')
        else:
            error_message = "Invalid username or password."

    return render(request, 'accounts/admin_login.html', {'error_message': error_message})
