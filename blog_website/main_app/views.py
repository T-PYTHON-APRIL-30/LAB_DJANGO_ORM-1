from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from.models import post


# Create your views here.

def post_list(request):
    post=post.object.fillter(is_published=True).order_by('-published_date')
    return render(request,'blog/post_list.html',{'post:posts'})

def post_add(request:HttpRequest):
    post_add=post.objects.filter(is_published=True)
    return render(request, "main_app/post_add.html",{"post_app":post_add})     