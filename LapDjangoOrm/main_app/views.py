from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def add_post(request:HttpRequest):

    if request.method == "POST":
        #addin a new post in database
        new_post = Post(title=request.POST["title"], description=request.POST["description"], release_date=request.POST["release_date"], is_published=request.POST["is_published"])
        new_post.save()
        return redirect("main_app:index_page")

    return render(request, "main_app/add_post.html")



def index_page(request:HttpRequest):
    

    post = Post.objects.all()

    return render(request, "main_app/index.html", {"post" : post})


def post_detail(request:HttpRequest, post_id):

    post = Post.objects.get(id=post_id)

    return render(request, 'main_app/post_detail.html', {"post" : post})


def update_post(request:HttpRequest, post_id):

    post = Post.objects.get(id=post_id)
    iso_date = post.release_date.isoformat()

    #updating the post
    if request.method == "POST":
        Post.title = request.POST["title"]
        Post.description = request.POST["description"]
        Post.rating = request.POST["rating"]
        Post.release_date = request.POST["release_date"]
        Post.is_published = request.POST["is_published"]
        Post.save()

        return redirect("main_app:game_detail", game_id=game.id)

    return render(request, 'main_app/update_post.html', {"post" : Post, "iso_date" : iso_date})



def delete_post(request:HttpRequest, post_id):
    
    post = Post.objects.get(id=post_id)
    Post.delete()

    return redirect("main_app:index_page")


def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    post = Post.objects.filter(title__contains=search_phrase,)

    return render(request, "main_app/search_page.html", {"post" : post})