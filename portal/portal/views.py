from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect




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
    return render(request,'frontend/website/index.html')
def category(request):
    return render(request,'frontend/website/index.html')
def news(request):
    return render(request,'frontend/website/index.html')