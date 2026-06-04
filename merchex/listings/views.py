from django.http import HttpResponse
from django.shortcuts import render
from .models import Band
from .models import Listings

# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
                        <h1>Bonjour Django</h1>
                        <p>Mes goupes preferer sont :</p>
                        <ul>
                            <li>{bands[0].name}</li>
                            <li>{bands[1].name}</li> 
                            <li>{bands[2].name}</li>   
                        </ul>
                        """)

def about(request):
    return HttpResponse('<h1>Apropos</h2> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1>')

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