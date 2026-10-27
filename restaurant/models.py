from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return self.name