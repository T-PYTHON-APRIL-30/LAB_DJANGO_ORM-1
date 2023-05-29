from django.urls import path
from . import views

app_name = "my_blog"

urlpatterns = [ 
    path("", views.show_page, name="show_page"),
    path("add/blog/",views.add_page,name="add_page")
]