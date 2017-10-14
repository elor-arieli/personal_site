from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'Elor/about.html')

def CV(requset):
    return render(requset,'Elor/CV.html')

def photography(request):
    return render(request,'Elor/photography.html')

def public_appearence(requset):
    return render(requset,'Elor/public_appearence.html')

def writing(requset):
    return render(requset,'Elor/writing.html')