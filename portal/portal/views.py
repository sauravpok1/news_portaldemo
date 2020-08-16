from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from newsportal.models import Category, News
from django.contrib.auth.models import User
from contactus.models import contactus
from contactus.forms import contactForm
from django.db.models import Count
# imports here!!
import pandas as pd
import numpy as np
import nltk as nltk
# nltk.download ('all')
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from pip._vendor import requests
from sklearn import model_selection,svm
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


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



def dashboard(request):
    # no_user = User.objects.filter(is_active=True).aggregate(Count('id'))
    category = Category.objects.all().aggregate(Count('id'))
    print(category['id__count'])
    news = News.objects.all().aggregate(Count('id'))
    # no_message =contactus.objects.filter(status=False).all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=47bfe14abddce5050e694cabd6db30ed'
    city = 'kathmandu'
    city_weather = requests.get(url.format(city)).json()
    temperature = round((city_weather['main']['feels_like'] - 32) * 5 / 9, 2)
    max_temp = round((city_weather['main']['temp_max'] - 32) * 5 / 9, 2)
    # request the API data and convert the JSON to Python data types
    weather = {
        'city': city,
        'temperature': temperature,
        'max_temp': max_temp,
        'min_temp': round(temperature * 2 - max_temp, 2),
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {
        'category':category['id__count'],
        'news':news['id__count'],
        # 'no_message': no_message,
        'weather': weather,
    }
    return render(request,'backend/dashboard.html',context)


def signout(request):
    logout(request)
    return redirect('signin')

def home(request):
    menus = Category.objects.filter(status=1)
    main_news = News.objects.filter(status=1,main_news=1).order_by('-created_date')
    main1 = main_news.first()
    mains= main_news[1:3]

    cat1_news = News.objects.filter(category_id=menus.first().id, status=1).order_by('-created_date')[:3]
    cat2_news = News.objects.filter(category_id=menus[1].id, status=1).order_by('-created_date')[:1]
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

    paginator = Paginator(news_as_per_category, 3)

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'menus': menus,
        'news':news_as_per_category,
        'cat':cat,
        'posts':posts,
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

    descr = request.GET['desc']
    category = Category.objects.all()

    print(descr)
    try:
        filterationss = categorization(descr)
    except:
        opt = "<option selected>--Invalid Description To Filter--</option>"
        for cat in category:
            opt = opt + "<option value='" + str(cat.id) + "'>" + cat.title + "</option>"
        return JsonResponse({'data': opt})

    data = {
        'Prediction': filterationss,
        'return': 'from server'
    }
    opt = "<option>----</option>"

    for cat in category:
        if(cat.filteration == str(data['Prediction']) ):
            opt = opt + "<option value='" + str(cat.id) + "' selected>" + cat.title + "</option>"
        else:
         opt = opt+"<option value='"+str(cat.id)+"'>"+cat.title+"</option>"


    # print(opt)
    print(str(data['Prediction']))
    return JsonResponse({'data':opt})


    # news portal algotrithm

def filteration(description):
    # news portal algotrithm
    # CONVERTING INTO LOWERCASE:
    variable_name = description.lower()

    # TOKENIZATION\
    tokens = nltk.word_tokenize(variable_name)
    token_words = [w for w in tokens if w.isalpha()]

    # STOPWORDS:
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in token_words if not w in stops]

    # STEMMING:
    stemming = nltk.PorterStemmer()
    stemmed_list = [stemming.stem(word) for word in meaningful_words]

    # REJOIN  WORDS:
    joined_words = (",".join(stemmed_list))

    return joined_words

def data_split(df):

  Description = np.array(df['Description'].values.astype('U'))
  Label = np.array(df['Label'].values.astype('U'))

  return Description,Label



def categorization( description_text,):
    data = {'user_data': [description_text]
            }
    decription_dataset = pd.DataFrame(data, columns=['user_data'])
    decription_dataset['user_data'] = decription_dataset['user_data'].apply(filteration)
    # print(len(text_dataset['datas'][0].split(',',100000)))
    # ONLY FOR LRNGTH
    # print('2')
    description_filtered = filteration(description_text)
    description_filtered_string = str(description_filtered)
    description_filtered_list = description_filtered_string.split(',', 100000)
    # list2 = []
    # list2.append(descr)
    # # print(list2)
    # desc = pd.DataFrame(descr)
    description_filtered_list_length = len(description_filtered_list)
    # print(len(desc))

    Tfidf_length = TfidfVectorizer(encoding='utf-8', max_features=description_filtered_list_length)
    data_length = Tfidf_length.fit_transform(decription_dataset['user_data']).toarray()  # [1,[X]]
    length_max_features = len(data_length[0])

    corpus = pd.read_csv("newsportal/dataset/train_test_data.csv")
    corpus = shuffle(corpus)


    # TEST_TRAIN_DATA
    X_train, X_test, Y_train, Y_test = train_test_split(corpus['filtered_description'], corpus['label'], test_size=0.2)

    # TFIDF of TEST_TRAIN data
    Tfidf = TfidfVectorizer(encoding='utf-8', max_features=length_max_features)
    Train_X_Tfidf = Tfidf.fit_transform(X_train).toarray()
    Test_X_Tfidf = Tfidf.transform(X_test).toarray()
    # TFIDF of descr
    Tfidf_descr = TfidfVectorizer(encoding='utf-8', max_features=length_max_features)

    descrption_Tfidf = Tfidf_descr.fit_transform(decription_dataset['user_data']).toarray()  # [1,[X]]

    # print(len(descr_Tfidf))

    # SVM algorithm part
    SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
    SVM.fit(Train_X_Tfidf, Y_train)
    predictions_SVM = SVM.predict(descrption_Tfidf)
    prediction_SVM = SVM.predict(Test_X_Tfidf)
    print("SVM Accuracy Score -> ", accuracy_score(prediction_SVM, Y_test) * 100)

    return predictions_SVM










