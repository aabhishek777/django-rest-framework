
from rest_framework import generics

from .models import Products
from .serializers import ProductSerializes


# this is class based view

class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializes


class ProductCreateAPIView(generics.CreateAPIView):
    '''

    this is used to create the product . we can pass the data in body also we will use POST Req

    '''

    queryset = Products.objects.all()
    serializer_class = ProductSerializes


class ProductListCreateAPIView(generics.ListCreateAPIView):
    '''
    GET Req

    '''
    queryset = Products.objects.all()
    serializer_class = ProductSerializes

    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if not content:
            content = title
        serializer.save(content=content)


# function based view
