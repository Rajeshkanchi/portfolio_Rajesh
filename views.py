from django.shortcuts import render

from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader


def home(request):
    return render(request,'first_page.html')


def contact(request):
    if request.method =="POST":
        name= request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        describe = request.POST.get('describe')
        contact= Contact(name=name,email=email,phone=phone,describe=describe,date=datetime.today())
        contact.save()
        message.success(request, 'Query sent succesfullyy.')
    return render(request,'contact.html')

def first_page(request):
    return render(request,'first_page.html')

def About_Me(request):
    return render(request,'About_Me.html')

def Work(request):
    return render(request,'Work.html')
