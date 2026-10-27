from django.urls import path

from .views import (
    index,
    MenuListCreateView,
    BookingListCreateView,
    BookingDetailView,
    RegistrationView,
)

urlpatterns = [
    # Home page
    path(
        '',
        index,
        name='index'
    ),

    # Menu API
    path(
        'menu/',
        MenuListCreateView.as_view(),
        name='menu'
    ),

    # Booking API
    path(
        'bookings/',
        BookingListCreateView.as_view(),
        name='bookings'
    ),

    # Single booking: GET, PUT, DELETE
    path(
        'bookings/<int:pk>/',
        BookingDetailView.as_view(),
        name='booking-detail'
    ),

    # User registration
    path(
        'registration/',
        RegistrationView.as_view(),
        name='registration'
    ),
]