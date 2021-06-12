from django.urls import path
from .views import WeatherCreate, WeatherList


urlpatterns = [
    path('create/', WeatherCreate.as_view(), name='create-weather'),
    path('', WeatherList.as_view()),
]