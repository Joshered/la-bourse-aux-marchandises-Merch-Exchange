from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1 style="color:green">Apropos</h1><br /> <p>Nous adoros cette app</p>')
    
