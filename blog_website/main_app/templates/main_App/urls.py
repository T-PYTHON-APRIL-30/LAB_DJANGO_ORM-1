from django.urls import path
from .views import post_list,post_add


urlpattsrns=[
    path('',post_list, name='post_list'),
    path('add/',post_add, name='post_add'),
]