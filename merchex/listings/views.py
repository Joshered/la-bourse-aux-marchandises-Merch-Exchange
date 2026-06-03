from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')

def about(request):
    return HttpResponse('<h1>Apropos</h2> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1>')

