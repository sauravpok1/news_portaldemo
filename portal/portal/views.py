from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from newsportal.models import Category, News

from contactus.forms import contactForm
# imports here!!
import pandas as pd
import nltk as nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


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

    cat1_news = News.objects.filter(category_id=menus.first().id, status=1).order_by('-created_date')[:3]
    cat2_news = News.objects.filter(category_id=menus[1].id, status=1).order_by('-created_date')[:2]
    cat3_news = News.objects.filter(category_id=menus[2].id, status=1).order_by('-created_date')[:5]
    cat4_news = News.objects.filter(category_id=menus[3].id, status=1).order_by('-created_date')[:4]
    head_list = {
        'title1': menus[0].title,
        'slug1': menus[0].slug,
        'title2': menus[1].title,
        'slug2': menus[1].slug,
        'title3': menus[2].title,
        'slug3': menus[2].slug,
        'title4': menus[3].title,
        'slug4': menus[3].slug,
        'title5': menus[4].title,
        'slug5': menus[4].slug,
    }

    context = {
       'menus':menus,
       'head_list':head_list,

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
        'news':news_as_per_category,
        'cat':cat,
    }

    return render(request,'frontend/website/list.html',context)
def news(request,slug):
    menus = Category.objects.filter(status=1)
    news = News.objects.get(slug=slug)


    context = {
        'menus': menus,
        'news': news,
    }
    return render(request,'frontend/website/second.html',context)
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

def main_news(request):
    menus = Category.objects.filter(status=1)
    main_news = News.objects.filter(status=1, main_news=1).order_by('-created_date')


    context = {
        'menus': menus,
        'main_news': main_news,

    }

    return render(request,'frontend/website/main_news.html',context)


def news_category_ajax(request):
    description = request.GET.get('desc')

    # news portal algotrithm
    # CONVERTING INTO LOWERCASE:
    variable_name = description.lower()

    # TOKENIZATION:

    tokens = nltk.word_tokenize(variable_name)
    token_words = [w for w in tokens if w.isalpha()]


    # STEMMING:
    stemming = nltk.PorterStemmer()
    stemmed_list = [stemming.stem(word) for word in token_words]


    #STOPWORDS:
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in stemmed_list if not w in stops]

    

    # REJOIN  WORDS:
    joined_words = (" ".join(meaningful_words))
    print(joined_words)







    data = {
        'desc': joined_words,
        'return':'from server'
    }
    return JsonResponse(data)