"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('backend/dashboard/', views.dashboard, name='dashboard'),
    path('backend/crud/',include('newsportal.urls')),

    path('', views.home, name='home'),
    path('main_news/', views.main_news, name='main_news'),
    path('category/<slug>', views.category, name='category'),
    path('news/<slug>', views.news, name='news'),
    path('contactus/', views.contactus, name='contactus'),
    # ajax
    path('news_category_ajax/', views.news_category_ajax, name='news_category_ajax'),



    path('backend/contactus/', include('contactus.urls')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)