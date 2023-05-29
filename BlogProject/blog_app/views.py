from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Blog

# Create your views here.

def home_page(request:HttpRequest):
    blogs = Blog.objects.all()

    return render(request,"blog_app/home.html",{"blogs": blogs} )

def add_blog(request:HttpRequest):
    if request.method == "POST":
        #addin a new blog in database
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("blog_app:home_page")

    return render(request,"blog_app/add_blog.html" )
