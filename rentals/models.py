from django.db import models

# Create your models here.
class Rental(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    image = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
