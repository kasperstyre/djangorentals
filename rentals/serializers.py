from rest_framework import serializers
from rentals.models import Rental

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['id', 'title', 'owner', 'city', 'category', 'bedrooms', 'image', 'description']