from django.urls import path
from . import views


app_name = 'main_app'


urlpatterns = [
    path("", views.add_blog, name="add_blog"),
    path("read/", views.read_blog, name="read_blog"),
    path("read/detail/<i_id>/", views.detail_blog, name="detail_blog"),
    path("detail/update/<i_id>/", views.update_blog, name="update_blog"),
    path("detail/delete/<i_id>/", views.delete_blog, name="delete_blog"),
    path("read/search/", views.search_page, name="search_page"),
    ]