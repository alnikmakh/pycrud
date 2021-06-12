from django.shortcuts import render
from .models import Weather
from rest_framework import generics
from .serializers import WeatherSerializer


class WeatherCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Weather.objects.all(),
    serializer_class = WeatherSerializer


class WeatherList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
