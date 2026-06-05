from django.http import HttpResponse
from django.shortcuts import render
from .models import Band
from .models import Listings

# POur les groupe.
def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html')

def about(request):
    return HttpResponse('<h1>Apropos</h2> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1>')

# POUR LES LISTings
def listings(request):
    listing = Listings.objects.all()
    return HttpResponse(f"""
                        <h1>Nos listings</h1>
                        <ul>
                        <li> {listing[0].title} </li>
                        <li> {listing[1].title} </li>
                        <li> {listing[2].title} </li>
                        </ul>
                        """)