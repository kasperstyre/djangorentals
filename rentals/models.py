from django.db import models

communityProperties = ['Condo', 'Townhouse', 'Apartment']

# Create your models here.
class Rental(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    image = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + " - " + self.city

    def is_community_property(self):
        return self.category in communityProperties

class RentalList():
    def __init__(self, rentals):
        self.rentals = rentals