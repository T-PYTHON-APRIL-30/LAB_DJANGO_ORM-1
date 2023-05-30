from django.shortcuts import render, redirect
from .models import Post
from .forms import Form

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:home')
    else:
        form = Form()
    return render(request, 'add_post.html', {'form': form})