from django.urls import path
from . import views

app_name = "blog_app"

urlpatterns = [
    path('', views.home_page , name="home_page"),
    path("blog", views.add_blog , name="add_blog"),
    path("read/<blog_id>/", views.read_blog , name="read_blog"),
    path("update/<blog_id>/", views.update_blog , name="update_blog"),
]