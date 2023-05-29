from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.shortcuts import resolve_url
from .models import blog
# Create your views here.

def home_page(request:HttpRequest):
    blogs =blog.objects.all()
    return render(request,"main_app/index.html",{"blogs" : blogs})


def add_page(request:HttpRequest):
    if request.method == "POST":
        
        new_blog = blog(title=request.POST["title"], Content=request.POST["Content"],  is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("main_app:home_page")
    
    return render(request,"main_app/add.html")
    