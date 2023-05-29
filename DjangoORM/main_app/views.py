from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Blog
from datetime import date


# Create your views here.
def home(request: HttpRequest):
    blog = Blog.objects.all()

    return render(request, 'main_app/home.html', {"blog" : blog})


def post_page(request: HttpRequest):
    if request.method == "POST":
        today = date.today()

        new_blog = Blog( tital = request.POST["tital"], content = request.POST["content"], is_published = request.POST["is_published"], publish_date = today )
        new_blog.save()

        return redirect("main_app:home")

    return render(request, 'main_app/post.html')
