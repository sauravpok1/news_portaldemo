from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import contactus


@login_required(login_url='signin')
def create_contactus(request):
    data = contactus.objects.all().order_by('status')
    context = {
        'messages': data
    }
    return render(request, 'backend/contactus/list.html', context)

def list_contactus(request):
    data = contactus.objects.all()
    context = {
        'messages': data,

    }
    return render(request, 'backend/contactus/list.html', context)


def delete_contactus(request, id):
    contact = contactus.objects.get(pk=id)
    contact.delete()
    messages.add_message(request, messages.SUCCESS, "Message successfully deleted")
    return redirect('message')

