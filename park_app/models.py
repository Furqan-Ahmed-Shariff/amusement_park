from django.db import models


# Create your models here.
class Show(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)
    Duration = models.IntegerField()

    def __str__(self):
        return f"{self.Name}"


class Showing(models.Model):
    StartTime = models.TimeField()
    ShowID = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="showings")

    def __str__(self):
        return f"{self.ShowID} at {self.StartTime}"


class Ride(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)
    MinimumHeight = models.IntegerField()
    Duration = models.IntegerField()
    MaximumCapacity = models.IntegerField()

    def __str__(self):
        return f"{self.Name}"


class Visitor(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    TicketNo = models.IntegerField()
    Age = models.IntegerField()
    Parking_used = models.BooleanField()
    BookedShow = models.ManyToManyField(Showing, blank=True, related_name="audience")
    BookedRide = models.ManyToManyField(Ride, blank=True, related_name="participants")

    def __str__(self):
        return f"{self.FirstName}"


class Stall(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=100, default="It's a Stall")
    Type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.Name}"


class Worker(models.Model):
    Name = models.CharField(max_length=20)
    StallID = models.ForeignKey(
        Stall, on_delete=models.CASCADE, related_name="workers", blank=True
    )
    RideID = models.ForeignKey(
        Ride, on_delete=models.CASCADE, related_name="controllers", blank=True
    )

    def __str__(self):
        return f"{self.Name}"
