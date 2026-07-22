from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('associate-login/', views.associate_login, name='associate_login'),
    path('login/', views.user_login_view, name='login'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('signup/', views.signup_view, name='signup'),
 
]