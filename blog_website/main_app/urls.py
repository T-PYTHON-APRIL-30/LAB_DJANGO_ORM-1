from django.urls import path
from .templates.main_App import views

app_name='main_app'
urlpattsrns=[
    path('',views.post_list, name='post_list'),
    path('add/',views.post_add, name='post_add'),
]