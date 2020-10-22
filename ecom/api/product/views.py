from django.shortcuts import render
from .serializers import Product, ProductSerializers
from rest_framework import viewsets
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializers
