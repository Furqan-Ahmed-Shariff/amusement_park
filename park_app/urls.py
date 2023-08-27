from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('rides', views.rides, name="rides"),
    path('stalls', views.stalls, name="stalls"),
    path('shows', views.shows, name="shows"),
]