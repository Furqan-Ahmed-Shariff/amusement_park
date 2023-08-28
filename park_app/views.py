from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    return render(request, "park_app/index.html")


def rides(request):
    return render(request, "park_app/rides.html", {"rides": Ride.objects.all()})


def stalls(request):
    return render(request, "park_app/stalls.html", {"stalls": Stall.objects.all()})


def shows(request):
    return render(request, "park_app/shows.html", {"shows": Show.objects.all()})


def ride(request, ride_id):
    render(request, "park_app/ride.html", {"ride": Ride.objects.get(pk=ride_id)})


def show(request, show_id):
    render(
        request,
        "park_app/show.html",
        {
            "show": Show.objects.get(pk=show_id),
            "showings": Showing.objects.filter(ShowID=show_id),
        },
    )


def stall(request, stall_id):
    render(request, "park_app/stall.html", {"stall": Stall.objects.get(pk=stall_id)})
