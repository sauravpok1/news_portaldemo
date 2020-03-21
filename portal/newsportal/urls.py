from django import views
from django.urls import path

from .import views


urlpatterns = [
    path('create',views.create_category, name='create_category'),
path('create',views.list_category, name='list_category'),
path('create',views.delete_category, name='delete_category'),
path('create',views.edit_category, name='edit_category')
]