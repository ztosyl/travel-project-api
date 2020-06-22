from django.db import models

from .plans import Plan

# Create your models here.
class Itinerary(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  date = models.DateField(max_length=100)
  duration = models.CharField(max_length=100)
  point_of_interest = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=100000)
  plan = models.ForeignKey(
      Plan,
      on_delete=models.CASCADE
  )
