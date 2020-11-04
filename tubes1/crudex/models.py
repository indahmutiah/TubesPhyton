from django.db import models

# Create your models here.
class Product(models.Model):
    product_value=models.CharField(max_length=100)
    def __str__(self):
        return self.product_value