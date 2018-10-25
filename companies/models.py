from django.db import models
from django_countries.fields import CountryField


class Company(models.Model):
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    country = CountryField()
    email = models.EmailField()

    def __str__(self):
        return self.company
