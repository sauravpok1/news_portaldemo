from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:id>', views.delete_contactus, name='delete_contactus'),
    path('list/', views.list_contactus, name='list_contactus'),

]