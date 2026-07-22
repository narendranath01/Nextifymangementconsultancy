# Register your models here.
# accounts/admin.py
# accounts/admin.py
from django.contrib import admin
from .models import CustomUser, UserProfile, AssociateProfile, AdminProfile

admin.site.site_header = "Nextify Admin"
admin.site.index_title = "Welcome to Nextify Admin Portal"
admin.site.site_title = "Nextify Management Consultant"


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'phone_number', 'business_name')
    search_fields = ('username', 'email', 'business_name')
    list_filter = ('user_type',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'address')
    search_fields = ('user__username', 'address')

@admin.register(AssociateProfile)
class AssociateProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'role', 'joining_date')
    search_fields = ('user__username', 'department', 'role')

@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'admin_level')
    search_fields = ('user__username', 'admin_level')