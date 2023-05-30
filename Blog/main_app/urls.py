from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.home, name = "home"),
    path('add_post/', views.add_post, name='add_post'),
]