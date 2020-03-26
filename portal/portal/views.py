from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from newsportal.models import Category, News




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

    context = {
       'menus':menus
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