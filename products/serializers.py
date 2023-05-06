from rest_framework import serializers
from .models import Products


class ShortDateSerializerField(serializers.DateTimeField):
    def to_representation(self, value):
        return value.strftime("%Y/%m/%d")

class GetProductsSerializer(serializers.ModelSerializer):
    created_at = ShortDateSerializerField()
    updated_at = ShortDateSerializerField()
    class Meta:
        model = Products
        fields = '__all__'
