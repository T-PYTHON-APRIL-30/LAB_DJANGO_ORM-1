from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.

def add_blog(request:HttpRequest):
    if request.method == "POST":
            new_blog = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"])
            new_blog.save()
            return redirect("main_app:read_blog")
    return render (request, "main_app/add_blog.html")

def read_blog(request:HttpRequest):
    read_blog = Post.objects.filter(is_published=True)
    return render(request, "main_app/read_blog.html", {"read_blog" : read_blog})