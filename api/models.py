from django.db import models

class ProductAvailability(models.Model):  
    product_id = models.CharField(max_length=255)
    unavailable_dates = models.JSONField(default=list) 
    

    def __str__(self):
        return f"Availability for Product ID: {self.product_id}"