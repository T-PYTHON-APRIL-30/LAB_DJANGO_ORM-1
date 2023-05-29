from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import blog

# Create your views here.

def read_blog(request:HttpRequest):

    blogs = blog.objects.all()
    
    return render(request, "solution/blog_read.html", {"blogs":blogs})

def add_blog(request:HttpRequest):

    if request.method == "POST":
        new_blog = blog(title=request.POST["title"], description=request.POST["description"])
        new_blog.save()
        return redirect("solution:read_blog")

    return render(request, "solution/blog_add.html")
