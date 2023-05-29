from django.urls import path
from . import views

app_name= "main_app"

urlpatterns=[
    path("blog/add/",views.add_blog,name="add_blog"),
    path("",views.read_blog,name="read_blog")
]