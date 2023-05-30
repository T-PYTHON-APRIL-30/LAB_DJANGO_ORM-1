from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import blog

# Create your views here.

def home_page(request:HttpRequest):
    return redirect("solution:read_blog")

def read_blog(request:HttpRequest):

    blogs = blog.objects.all()
    
    return render(request, "solution/blog_read.html", {"blogs":blogs})

def add_blog(request:HttpRequest):

    if request.method == "POST":
        new_blog = blog(title=request.POST["title"], context=request.POST["context"], is_published=request.POST["is_published"], publish_date = request.POST["publish_date"] )
        new_blog.save()
        return redirect("solution:read_blog")

    return render(request, "solution/blog_add.html")
