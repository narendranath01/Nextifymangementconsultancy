from django.contrib import admin
from .models import Blog

admin.site.site_header = "Nextify Admin"
admin.site.index_title = "Welcome to Nextify Admin Portal"
admin.site.site_title = "Nextify Management Consultant"


admin.site.register(Blog)
