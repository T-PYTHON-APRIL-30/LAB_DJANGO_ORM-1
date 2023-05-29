from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from.models import post
from.forms import PostForm 

# Create your views here.

def post_list(request):
    post=post.object.fillter(is_published=True).order_by('-published_date')
    return render(request,'blog/post_list.html',{'post:posts'})

def post_add(request):
    if request.method=='POST':
     form=PostForm(request.POST)
     if forms.is_valid():
        form.save()
        return redirect('post_list')
     else:
        form =PostForm()
        return render(request,'blog/post_add.html',{'form':form})
     