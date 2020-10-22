from os import name

from api.product.models import Product
from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')
