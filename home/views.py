from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
          'variable':"This is sent",
          'variable1':"Kamal is great"
    }
    
    return render(request,'home/index.html',context)

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'All data is stored successfully...')    
    return render(request,'home/contact.html')

def services(request):
    return render(request,'home/services.html')    

    