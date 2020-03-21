from django import views
from django.urls import path

from .import views


urlpatterns = [
    path('create',views.create_category, name='create_category'),
    path('list',views.list_category, name='list_category'),
    path('<int:id>/delete',views.delete_category, name='delete_category'),
    path('<int:id>/edit',views.edit_category, name='edit_category')
]