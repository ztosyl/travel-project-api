from django.db import models

from .user import User

# Create your models here.
class Plan(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  destination = models.CharField(max_length=100)
  dep_airport_code = models.CharField(max_length=3)
  arr_airport_code = models.CharField(max_length=3)
  # flight TO destination departure time
  flight_to_dep_time = models.TimeField()
  # flight TO destination arrival time
  flight_to_arr_time = models.TimeField()
  # flight FROM destination departure time
  flight_from_dep_time = models.TimeField()
  # flight FROM destination arrival time
  flight_from_arr_time = models.TimeField()
  hotel_name = models.CharField(max_length=100)
  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )
