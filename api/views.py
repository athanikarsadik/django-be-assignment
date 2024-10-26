from django.shortcuts import render
from rest_framework import generics
from .models import ProductAvailability
from .serializers import ProductAvailabilitySerializer

class ProductAvailabilityGetCreate(generics.ListCreateAPIView):
    queryset = ProductAvailability.objects.all()
    serializer_class = ProductAvailabilitySerializer
    
class ProductAvailabilityRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = ProductAvailability.objects.all()
    serializer_class = ProductAvailabilitySerializer
    lookup_field = 'product_id' 