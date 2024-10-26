from rest_framework import serializers
from .models import ProductAvailability

class ProductAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAvailability
        fields = '__all__'