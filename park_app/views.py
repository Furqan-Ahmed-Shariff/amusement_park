from django.shortcuts import render
from django.http import HttpResponse
from models import *

# Create your views here.
def index(request):
    return render(request, "park_app/index.html")

def rides(request):
    return render(request, "park_app/rides.html", {"rides": Ride.objects.all()})

def stalls(request):
    return render(request, "park_app/stalls.html", {"stalls": Stall.objects.all()})

def shows(request):
    return render(request, "park_app/shows.html", {"shows": Show.objects.all()})