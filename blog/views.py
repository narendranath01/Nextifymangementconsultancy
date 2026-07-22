from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test

from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='associates').exists())
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('blog_detail', blog_id=blog.id)
    return render(request, 'blog/edit_blog.html', {'blog': blog})


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

