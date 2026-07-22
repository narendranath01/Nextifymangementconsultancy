from django.urls import path
from . import views

urlpatterns = [
      # Home Page
    path('', views.home, name='home'),

    # About Page
    path('about/', views.about, name='about'),

    # Services Pages
    path('business-analytics/', views.business_analytics, name='businessanalytics'),
    path('finance-analytics/', views.finance_analytics, name='financeanalytics'),
    path('market-analytics/', views.market_analytics, name='marketanalytics'),
    path('market-research/', views.market_research, name='marketresearch'),
    path('seo/', views.seo, name='seo'),
    path('management-consulting/', views.management_consulting, name='managementconsulting'),
    path('organizational-development/', views.organizational_development, name='orgdevelopment'),
    path('risk-management/', views.risk_management, name='riskmanagement'),
    path('strategic-planning/', views.strategic_planning, name='strategicplanning'),
    path('change-management/', views.change_management, name='changemanagement'),
    path('other-services/', views.other_services, name='others'),
    path('finance/', views.finance, name='finance'),
    # Contact Page
    path('contact-us/', views.contact_us, name='contactus'),

    # Authentication paths
    path("login/", views.login_view, name='login'),  # Generic login view
    path("signup/", views.signup_view, name='signup'),  # Signup view
]
