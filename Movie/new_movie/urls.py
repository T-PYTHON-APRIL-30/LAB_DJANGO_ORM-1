from django.urls import path
from . import views


app_name = "new_movie"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("add/", views.add_page , name="add_page"),
    path("view/", views.view_page , name="view_page")

]