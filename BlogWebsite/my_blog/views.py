from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Blog

# Create your views here.

def show_page(request:HttpRequest):

    blogs = Blog.objects.all()

    return render(request,"my_blog/show_page.html", {"blogs" : blogs})

def add_page(request:HttpRequest):

    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"])
        new_blog.save()
        return redirect("my_blog:show_page")
    
    return render(request,"my_blog/add_page.html")