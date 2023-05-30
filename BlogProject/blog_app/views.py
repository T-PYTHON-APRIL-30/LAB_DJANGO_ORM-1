from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Blog

# Create your views here.

def home_page(request:HttpRequest):
    blogs = Blog.objects.filter(is_published="True")

    return render(request,"blog_app/home.html",{"blogs": blogs} )

def add_blog(request:HttpRequest):
    if request.method == "POST":
        #addin a new blog in database
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("blog_app:home_page")

    return render(request,"blog_app/add_blog.html" )

def read_blog(request:HttpRequest, blog_id):
    blog =Blog.objects.get(id=blog_id)

    return render(request,'blog_app/read.html',{"blog": blog} )


def update_blog(request:HttpRequest,blog_id):
    blog =Blog.objects.get(id=blog_id)
    iso_date = blog.publish_date.isoformat()

    #updating
    if request.method == "POST":

        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.publish_date = request.POST["publish_date"]
        blog.save()
        return redirect("blog_app:read_blog", blog_id = blog.id)

    return render(request,"blog_app/update.html",{"blog":blog, "iso_date": iso_date} )
