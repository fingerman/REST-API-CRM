from rest_framework import serializers
from suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ('id', 'name', 'email', 'products')
