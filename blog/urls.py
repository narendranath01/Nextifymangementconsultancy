from django.urls import path
from .views import blog_list, blog_detail, edit_blog


urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<int:blog_id>/', blog_detail, name='blog_detail'),
    path('<int:blog_id>/edit/', edit_blog, name='edit_blog'),

]
