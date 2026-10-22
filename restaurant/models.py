from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100)
    no_of_guests = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    booking_date = models.DateField()
    booking_time = models.TimeField()

    class Meta:
        ordering = ["booking_date", "booking_time"]
        constraints = [models.UniqueConstraint(fields=["booking_date", "booking_time"], name="unique_booking_date_time")]

    def __str__(self):
        return f"{self.name} — {self.booking_date} {self.booking_time}"
