from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializers import (
    MenuSerializer,
    BookingSerializer,
    UserRegistrationSerializer,
)

def index(request):
    return render(request, 'index.html')
    
class MenuListCreateView(generics.ListCreateAPIView):
        queryset = Menu.objects.all()
        serializer_class = MenuSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class RegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = Token.objects.create(user=user)

        return Response(
            {
                'message': 'User registered successfully.',
                'token': token.key
            },
            status=status.HTTP_201_CREATED
        )