from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Blog

# Create your views here.
def add_blog(request:HttpRequest):

    if request.method=="POST":
        new_blog=Blog(Title=request.POST["Title"],Content=request.POST["Content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("main_app:blog_page")

    return render(request,"main_app/add_blog.html")

def blog_page(request:HttpRequest):

    blog=Blog.objects.all()

    return render(request,"main_app/blog_page.html",{"blog":blog})

