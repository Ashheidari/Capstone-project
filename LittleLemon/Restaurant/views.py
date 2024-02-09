from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializers import MenuItemSerilaizer, BookingSerilaizer, UserSerializer
# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerilaizer
    #permission_classes = [IsAuthenticated]



class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerilaizer



class BookingView (generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerilaizer
    permission_classes = [IsAuthenticated]
