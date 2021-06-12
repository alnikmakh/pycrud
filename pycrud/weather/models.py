from django.db import models

# Create your models here.
class Weather(models.Model):
    temperatureC = models.DecimalField(max_digits=4, decimal_places=2)
    pressure = models.PositiveSmallIntegerField()
    humidity = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)