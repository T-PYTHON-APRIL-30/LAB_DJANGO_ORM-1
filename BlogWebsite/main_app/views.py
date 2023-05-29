from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.

def home(request:HttpRequest):

    blogs = Blog.objects.all()

    return render(request, 'main_app/home.html', {'blogs' : blogs})

def add_blog(request:HttpRequest):

    if request.method == 'POST':
        new_blog = Blog(title = request.POST['title'], content = request.POST['content'],is_published=request.POST["is_published"], publish_date = request.POST['publish_date'])
        new_blog.save()
        return redirect('main_app:home')

    return render(request, 'main_app/add.html')

