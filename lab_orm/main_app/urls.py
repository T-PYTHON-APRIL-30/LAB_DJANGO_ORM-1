from django.urls import path
from . import views

app_name= "main_app"

urlpatterns= [
    path("",views.blog_page,name="blog_page"),
    path("blog/add",views.add_blog,name="add_blog")
]