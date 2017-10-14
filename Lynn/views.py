from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'Lynn/about.html')

def CV(requset):
    return render(requset,'Lynn/CV.html')

def MD(requset):
    return render(requset,'Lynn/MD.html')

def art(requset):
    return render(requset,'Lynn/art.html')

def photography(requset):
    return render(requset,'Lynn/photography.html')

def music(requset):
    return render(requset,'Lynn/music.html')