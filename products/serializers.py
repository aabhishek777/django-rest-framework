
from rest_framework import serializers
from .models import Products




class ProductSerializes(serializers.ModelSerializer):
    
    # my_discount= serializers.SerializerMethodField(read_only=True)
    
    get_discount= serializers.ReadOnlyField()
    class Meta:
        model= Products
        fields= ['id', 'title', 'content', 'price', 'sale_price', 'get_discount']
    
    # def get_my_discount(self, obj):
    #     return obj.get_discount()
    