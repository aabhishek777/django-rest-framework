
from rest_framework import viewsets
from products.models import Products
from .serializers import ProductSerializes


class ProductListViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductSerializes
    lookup_field = 'pk'
