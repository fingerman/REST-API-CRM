from django.shortcuts import render
from rest_framework import viewsets, permissions
from products.models import Product
from .serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


'''

add custom written permisson. Define the permission in 'utils' and import it. 
permission_classes = (IsOwnerOrReadOnly, )
'''