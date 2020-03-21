from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category

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
