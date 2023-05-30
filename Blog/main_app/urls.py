from . import views
from django.urls import path

app_name = 'main_app'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('posts/', views.postsPage, name='postsPage')
]


