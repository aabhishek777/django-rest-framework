
from rest_framework import serializers
from .models import Products

from rest_framework.reverse import reverse  # reverse gives the url (current)


class ProductSerializes(serializers.ModelSerializer):

    # my_discount= serializers.SerializerMethodField(read_only=True)

    discount = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Products
        fields = [
            'id',
            'content',
            'price',
            'sale_price',
            'discount',
            'title',
            'url',
            'email'
        ]

    # validation logic

    def validate_title(self, value):  # naming convention validate_ + name of the filed
        # title__iexact etc. it will be case in-sensitive
        queryset = Products.objects.filter(title__exact=value)
        if queryset.exists():
            raise serializers.ValidationError(f'{value} is already exist.')
        return value

    def create(self, validated_data):
        email = validated_data.pop('email')
        return super().create(validated_data)

    def get_url(self, obj):
        # return f'/api/v2/{obj.pk}'
        request = self.context.get('request')
        if not request:
            return None
        # automatically added -list, -detail when using router.register basename eg products
        return reverse("products-detail",  kwargs={'pk': obj.pk}, request=request)

    def get_discount(self, obj):
        return obj.discount
