from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.utils import timezone
# Create your views here.

def add_blog(request:HttpRequest):

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        is_published = bool(request.POST.get('is_published', False))
        publish_date_str = request.POST.get('publish_date')
        if publish_date_str:
            publish_date = timezone.datetime.fromisoformat(publish_date_str)
        else:
            publish_date = timezone.now()
        post = Post.objects.create(title=title, content=content, is_published=is_published, publish_date=publish_date)
        post.save()
        return redirect('main_app:read_blog')
    else:
        return render(request, "main_app/add_blog.html")


def read_blog(request:HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('publish_date')
    return render(request,"main_app/read_blog.html",{'posts': posts})