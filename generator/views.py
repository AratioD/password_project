from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("hello there world, fantastic world!")

def burgers(request):
    return HttpResponse("burgers are fantastic!")