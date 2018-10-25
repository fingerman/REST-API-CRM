from django.shortcuts import render
from rest_framework import viewsets
from suppliers.models import Supplier
from .serializers import SupplierSerializer


class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
