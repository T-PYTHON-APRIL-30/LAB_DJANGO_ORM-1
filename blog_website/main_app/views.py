from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from.models import post


# Create your views here.

def add_post(request:HttpRequest):
    if request.method == "POST":
            new_blog =new_blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"])
            new_blog.save()
            return redirect("main_app:add_post")
    return render (request, "main_app/add_blog.html")

def post_add(request:HttpRequest):

   
    return render(request, "main_app/post_add.html")     