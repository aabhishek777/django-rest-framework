
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


from .models import Products
from .serializers import ProductSerializes
from .permissions import IsStaffEditorPermission
from root.authentication import TokenAuthentication

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

    # for permissions we added these authentication and permission classes in DRF
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]
    # permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [IsStaffEditorPermission]

    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if not content:
            content = title
        serializer.save(content=content)


# function based view

@api_view(['GET', 'POST'])
def product_alternate_view(request, pk=None, *args, **kwargs):

    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(Products, pk=pk)
            data = ProductSerializes(obj, many=False).data
            return Response(data=data)
        queryset = Products.objects.all()
        data = ProductSerializes(queryset, many=True).data
        return Response(data)
    if request.method == "POST":
        # create data
        serializer = ProductSerializes(data=request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
        serializer.save()

        return Response(serializer.data)
    return Response({"msg": "invalid , Not good data"}, status=400)


# USING MIXINS WE Can directly specify HTTP methods

class ProductMixinAPIView(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializes
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):

        if not kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)

    def perform_create(self, serializer):

        # title = serializer.validated_data.get('title')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if not content:
            content = title
        serializer.save(content=content)


product_mixin_api_view = ProductMixinAPIView.as_view()
