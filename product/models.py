from django.db import models

# Create your models here.
from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=255)   
    desc = models.CharField(max_length=255)   
    image = models.FileField(upload_to="product/", null=True)   
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





