from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from rest_framework import serializers
from .models import Booking, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "category"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "name", "no_of_guests", "booking_date", "booking_time"]
        read_only_fields = ["id"]

    def validate_booking_date(self, value):
        if value < timezone.localdate():
            raise serializers.ValidationError("Booking date cannot be in the past.")
        return value

    def validate(self, attrs):
        date = attrs.get("booking_date", getattr(self.instance, "booking_date", None))
        time = attrs.get("booking_time", getattr(self.instance, "booking_time", None))
        qs = Booking.objects.filter(booking_date=date, booking_time=time)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if date and time and qs.exists():
            raise serializers.ValidationError("This date and time slot is already booked.")
        return attrs


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "password"]
        read_only_fields = ["id"]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
