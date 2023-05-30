from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Post

# Create your views here.

def homePage (request:HttpRequest):
    post = Post.objects.filter(is_published=True)
    return render(request, "main_app/home.html", {"post" : post})
    
     
def postsPage(request):

    if request.method == "POST":
            
        newPost= Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"])
        newPost.save()
        return redirect("main_app:homePage")
    
    return render (request,'main_app/post.html') 
