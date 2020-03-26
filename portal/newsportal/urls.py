from django import views
from django.urls import path

from .import views


urlpatterns = [
    path('category/create',views.create_category, name='create_category'),
    path('category/list',views.list_category, name='list_category'),
    path('category/<int:id>/delete',views.delete_category, name='delete_category'),
    path('category/<int:id>/edit',views.edit_category, name='edit_category'),

    path('news/create', views.create_news, name='create_news'),
    path('news/list', views.list_news, name='list_news'),
    path('news/<int:id>/delete', views.delete_news, name='delete_news'),
    path('news/<int:id>/edit', views.edit_news, name='edit_news'),
]