from django.http import HttpResponse
from django.shortcuts import render
from .models import Band
from .models import Listings

# POur les groupe.
def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html',{"bands":bands})

def about(request):
    return render(request,'listings/about.html')

def contact(request):
    return render(request,'listings/contact.html')

# POUR LES LISTings
def listings(request):
    listing = Listings.objects.all()
    return render(request,'listings/listings.html',{"listings":listing})