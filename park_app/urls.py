from django.urls import path, include
from . import views

app_name = "park_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("rides", views.rides, name="rides"),
    path("stalls", views.stalls, name="stalls"),
    path("shows", views.shows, name="shows"),
    path("<int:ride_id>", views.ride, name="ride"),
    path("<int:show_id>", views.show, name="show"),
    path("<int:stall_id>", views.stall, name="stall"),
]
