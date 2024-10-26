from django.contrib import admin
from django.urls import  path
from .views import ProductAvailabilityGetCreate, ProductAvailabilityRetrieveUpdate

urlpatterns = [
    path('availability/', ProductAvailabilityGetCreate.as_view(), name='product-availability-list-create'),
    path('availability/<str:product_id>/', ProductAvailabilityRetrieveUpdate.as_view(), name='product-availability-retrieve-update'),
]
