from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'Home/index.html')

def contact(requset):
    return render(requset,'Home/contact.html')

def travel(request):
    return render(request,'Home/travel.html')