from django.db import models


# Create your models here.
class ProductSearch(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=200)
    search_datetime = models.DateTimeField('date searched')
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_link = models.CharField(max_length=300)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_link = models.CharField(max_length=300)
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
