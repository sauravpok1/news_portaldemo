from django import views
from django.urls import path

from .import views


urlpatterns = [
    path('create',views.create_category, name='create_category'),
    path('list',views.list_category, name='list_category'),
    path('<int:id>/delete',views.delete_category, name='delete_category'),
    path('<int:id>/edit',views.edit_category, name='edit_category')



    path('news/', views.list_news, name='news'),
    path('news/create/', views.create_news, name='create_news'),
    path('news/delete/<int:id>', views.delete_news, name='delete_news'),
    path('news/edit/<int:id>', views.edit_news, name='edit_news'),
]