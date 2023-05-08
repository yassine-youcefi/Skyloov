from .models import Products, Cart
from rest_framework import serializers


class ShortDateSerializerField(serializers.DateTimeField):
    def to_representation(self, value):
        return value.strftime("%Y/%m/%d")

class GetProductsSerializer(serializers.ModelSerializer):
    created_at = ShortDateSerializerField()
    updated_at = ShortDateSerializerField()
    class Meta:
        model = Products
        fields = '__all__'



class GetCartSerializer(serializers.ModelSerializer):
    items = GetProductsSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['id', 'status', 'total', 'items', 'created_at', 'updated_at']
        
class PostCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['owner','status','items']


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['items']