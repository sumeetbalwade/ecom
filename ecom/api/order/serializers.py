from api.order.models import Order
from rest_framework import serializers


class OrderSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user')
