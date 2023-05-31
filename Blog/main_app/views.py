from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpRequest

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def add_post(request:HttpRequest):
    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        is_published = request.POST["is_published"]
        publish_date = request.POST["publish_date"]

        new_post = Post(Title=title, Content=content, is_published=is_published, publish_date=publish_date)
        
        new_post.save()
        
        return redirect('main_app:home') 
    else: 
        return render(request, 'add_post.html')



#    return render(request, 'blog/index.html', {'posts': posts})

#  return redirect('index')
    #else:
        #return render(request, 'blog/add_post.html')