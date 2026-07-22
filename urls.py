from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Include blog URLs
    path('accounts/', include('accounts.urls')),  # Include accounts URLs
    path('', include('Home.urls')),
]
