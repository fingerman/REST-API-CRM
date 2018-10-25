from rest_framework import serializers
from products.models import Product
from djmoney.settings import CURRENCY_CHOICES


class ProductSerializer(serializers.ModelSerializer):
    price_currency = serializers.ChoiceField(choices=CURRENCY_CHOICES)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'price_currency', 'company')
