
from rest_framework import serializers
from .models import Products

from rest_framework.reverse import reverse  # reverse gives the url (current)


class ProductSerializes(serializers.ModelSerializer):

    # my_discount= serializers.SerializerMethodField(read_only=True)

    discount = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Products
        fields = [
            'id',
            'content',
            'price',
            'sale_price',
            'discount',
            'title',
            'url'
        ]

    def get_url(self, obj):
        # return f'/api/v2/{obj.pk}'
        request = self.context.get('request')
        if not request:
            return None
        # autometically added -list, -detail when using router.register basename eg products
        return reverse("products-detail",  kwargs={'pk': obj.pk}, request=request)

    def get_discount(self, obj):
        return obj.discount
