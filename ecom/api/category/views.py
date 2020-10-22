from rest_framework import viewsets
from .models import Catergory
from .serializers import CategorySerializers
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Catergory.objects.all().order_by('name')
