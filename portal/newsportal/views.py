from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CategoryForm, NewsForm
from .models import Category, News


# Create your views here.
@login_required(login_url='signin')
def create_category(request):
    form= CategoryForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"Category Added Successfully")
        return redirect('list_category')
    context={
        'form':form
    }
    return render(request,'backend/category/create.html',context)


@login_required(login_url='signin')
def list_category(request):
    category = Category.objects.all()
    context = {
        'categories': category
    }
    return render(request, 'backend/category/list.html',context )




@login_required(login_url='signin')
def edit_category(request, id, ):
    category = Category.objects.get(pk=id)
    form=CategoryForm(request.POST or None,request.FILES or None, instance=category)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"Category Updated Successfully")
        return redirect('list_category')
    context = {
        'forms':form
    }
    return render(request, 'backend/category/edit.html',context)





@login_required(login_url='signin')
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,"Category Deleted Successfully")

    return redirect('list_category')







@login_required(login_url='signin')
def list_news(request):
    data = News.objects.all()[::-1]
    context = {
        'news': data
    }
    return render(request, 'backend/news/list.html', context)

@login_required(login_url='signin')
def create_news(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "News added successfully")
        return redirect('list_news')
    context = {
        'form': form
    }
    return render(request, 'backend/news/create.html', context)

@login_required(login_url='signin')
def edit_news(request, id):
    data = News.objects.get(pk=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "News updated successfully")
        return redirect('list_news')
    context = {
        'forms': form

    }
    return render(request, 'backend/news/edit.html', context)

@login_required(login_url='signin')
def delete_news(request, id):
    news = News.objects.get(pk=id)
    news.delete()
    messages.add_message(request, messages.SUCCESS, "News successfully deleted")
    return redirect('list_news')
