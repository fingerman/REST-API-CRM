from django.db import models
from djmoney.models.fields import MoneyField
from django_countries.fields import CountryField
from companies.models import Company


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='EUR')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
