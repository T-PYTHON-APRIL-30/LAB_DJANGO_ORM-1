from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import movie

# Create your views here.

def home_page(request:HttpRequest):

    

    return render(request, "new_movie/home.html")

def add_page(request:HttpRequest):
    if request.method == "POST":
        
        new_movie = movie(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"])
        new_movie.save()
        return redirect("new_movie:view_page")

    return render(request, "new_movie/add_page.html")

def view_page(request:HttpRequest):
     
    movies = movie.objects.all()

    return render(request, "new_movie/view_page.html", {"movies": movies})