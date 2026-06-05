from django.http import HttpResponse
from django.shortcuts import render
from .models import Band
from .models import Listings

# POUR LA PAGE D'ACCUEIL
def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html',{"bands":bands})

# POUR LES PAGES ABOUT
def about(request):
    return render(request,'listings/about.html')

# POUR LES PAGES CONTACT
def contact(request):
    return render(request,'listings/contact.html')

# POUR LES LISTINGS
def listings(request):
    listing = Listings.objects.all()
    return render(request,'listings/listings.html',{"listings":listing})