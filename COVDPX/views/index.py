from django.shortcuts import render
from django.http import HttpResponse


def profil(request):
    return render(request, "index/profil.html")


def home(request):
    return render(request,'index/home.html')


