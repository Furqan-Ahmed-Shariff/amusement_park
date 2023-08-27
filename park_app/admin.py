from django.contrib import admin
from .models import *
# Register your models here.
class RideAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Description','MinimumHeight', 'Duration', 'MaximumCapacity']

class ShowAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Description', 'Duration']

class ShowingAdmin(admin.ModelAdmin):
    list_display = ['id', 'StartTime', 'ShowID']

class VisitorAdmin(admin.ModelAdmin):
    list_display = ['id', 'FirstName', 'LastName', 'TicketNo','Age', 'Parking_used']
    filter_horizontal = ("BookedShow", 'BookedRide')

class StallAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Type']

class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'StallID', 'RideID']


admin.site.register(Show, ShowAdmin)
admin.site.register(Showing, ShowingAdmin)
admin.site.register(Ride, RideAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Stall, StallAdmin)
admin.site.register(Worker, WorkerAdmin)