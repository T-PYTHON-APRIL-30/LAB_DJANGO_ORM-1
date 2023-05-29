from .models import Post
from django.shortcuts import render, redirect

def home(request):
    if request.method == "POST":
        is_published = request.POST.get('is_published') == 'on'
        post_content = Post(title=request.POST['title'], content=request.POST['content'], is_published=is_published,
                            publish_date=request.POST['publish_date'])
        post_content.save()
        return redirect('blog_app:content')

    return render(request, "blog_app/home.html")


def read(request):
        reader = Post.objects.all()
        return render(request, "blog_app/content.html", {"reader": reader})

