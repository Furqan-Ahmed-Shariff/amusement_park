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
    ride_ins = Ride.objects.get(pk=ride_id)
    return render(
        request,
        "park_app/ride.html",
        {
            "ride": ride_ins,
            "participants": ride_ins.participants.all(),
            "controllers": ride_ins.controllers.all(),
        },
    )


def show(request, show_id):
    show_ins = Show.objects.get(pk=show_id)
    showings = show_ins.showings.all()
    show_dict = dict(show=show_ins, showings=showings)
    audience = []
    lenghts = []
    for i, showing in enumerate(showings):
        single_audience = showing.audience.all()
        audience.append(single_audience)
        lenghts.append(len(single_audience))
    show_dict["audiences"] = audience
    return render(
        request,
        "park_app/show.html",
        {"show": show_ins, "showings": showings},
    )


def stall(request, stall_id):
    stall_ins = Stall.objects.get(pk=stall_id)
    return render(
        request,
        "park_app/stall.html",
        {
            "stall": stall_ins,
            "workers": stall_ins.workers.all(),
        },
    )
