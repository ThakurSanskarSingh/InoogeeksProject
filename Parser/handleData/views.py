from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homePage(request):
    return  render(request,"index.html")

def parsing(request):
    return HttpResponse("hello world")