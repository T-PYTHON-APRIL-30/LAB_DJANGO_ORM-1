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
    read_blog = Post.objects.all()
    return render(request, "main_app/read_blog.html", {"read_blog" : read_blog})

def detail_blog(request:HttpRequest, i_id):
    detail_blo = Post.objects.get(id = i_id)
    return render(request, "main_app/detail_blog.html", {"detail_blo" : detail_blo})


def update_blog(request:HttpRequest, i_id):
    blog = Post.objects.get(id=i_id)
    iso_date = blog.publish_date.isoformat()
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.publish_date = request.POST["publish_date"]
        blog.is_published = request.POST["is_published"]
        blog.save()
        return redirect("main_app:detail_blog",  i_id = blog.id)
     
    return render (request, "main_app/update_blog.html", {'blog':blog, "iso_date" : iso_date})


def delete_blog (request:HttpRequest, i_id):
    blog = Post.objects.get(id=i_id)
    blog.delete()

    return redirect("main_app:read_blog")

def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    blogs = Post.objects.filter(title__contains=search_phrase,)

    return render(request, "main_app/search_page.html", {"blogs" : blogs})