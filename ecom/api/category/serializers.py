from rest_framework import serializers
from . import models


class CategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Catergory
        fields = ('name', 'description')
