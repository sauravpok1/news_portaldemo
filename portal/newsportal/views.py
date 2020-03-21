from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CategoryForm

# Create your views here.
def create_category(request):
    form= CategoryForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"Category Added Successfully")
        return redirect('dashboard')
    context={
        'form':form
    }
    return render(request,'backend/category/create.html',context)

def list_category(request):
    return render(request, 'backend/category/list.html' )
def edit_category(request):
    return render(request, 'backend/category/edit.html')
