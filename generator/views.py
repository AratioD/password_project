from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password':'sdfsdfsf'})


def burgers(request):
    return HttpResponse('<h1>burgers are fantastic!</h1>')
