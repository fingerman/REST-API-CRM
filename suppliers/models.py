from django.db import models
from products.models import Product


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

