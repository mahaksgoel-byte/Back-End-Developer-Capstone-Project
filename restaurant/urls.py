from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import BookingViewSet, LoginView, MenuItemViewSet, RegistrationView

router = DefaultRouter()
router.register("menu", MenuItemViewSet, basename="menu")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = [
    path("", include(router.urls)),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("token/login/", LoginView.as_view(), name="token-login"),
]
