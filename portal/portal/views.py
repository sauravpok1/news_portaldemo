from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from newsportal.models import Category, News

from contactus.forms import contactForm


def signin(request):
    if request.method=='GET':
        return render(request, 'backend/signin.html')
    else:
        uname=request.POST.get('username')
        pswd= request.POST.get('password')
        user = authenticate(username=uname,password=pswd)
        if user is not None:
            login(request,user) #session rakhna ko lagi
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"Username or Password doesn't match")
            return redirect('signin')

# login requ
def dashboard(request):
    return render(request,'backend/dashboard.html')


def signout(request):
    logout(request)
    return redirect('signin')

def home(request):
    menus = Category.objects.filter(status=1)
    main_news = News.objects.filter(status=1,main_news=1).order_by('-created_date')
    main1 = main_news.first()
    mains= main_news[1:3]

    cat1_news = News.objects.filter(category_id=menus.first().id, status=1).order_by('-created_date')
    cat2_news = News.objects.filter(category_id=menus[1].id, status=1).order_by('-created_date')
    cat3_news = News.objects.filter(category_id=menus[2].id, status=1).order_by('-created_date')
    cat4_news = News.objects.filter(category_id=menus[3].id, status=1).order_by('-created_date')

    context = {
       'menus':menus,
        'main1':main1,
        'mains':mains,
        'cat1_news':cat1_news,
        'cat2_news': cat2_news,
        'cat3_news':cat3_news,
        'cat4_news': cat4_news,

    }
    return render(request,'frontend/website/index.html',context)
def category(request,slug):
    menus = Category.objects.filter(status=1)
    cat = Category.objects.get(slug=slug)
    news_as_per_category = News.objects.filter(category_id=cat.id, status=1)

    context = {
        'menus': menus,
        'news':news_as_per_category
    }

    return render(request,'frontend/website/list.html',context)
def news(request):
    menus = Category.objects.filter(status=1)

    context = {
        'menus': menus
    }
    return render(request,'frontend/website/index.html',context)
def contactus(request):
    menus = Category.objects.filter(status=1)
    form=contactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, " Feedback sent Successfully")
        return redirect('contactus')

    context = {
        'menus': menus,
        'forms':form
    }
    return render(request,'frontend/website/contactus.html',context)

