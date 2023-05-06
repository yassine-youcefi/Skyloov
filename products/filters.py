from django_filters import rest_framework as filters
from django_filters.filters import OrderingFilter
from .models import Products


class ProductsFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    brand = filters.CharFilter(lookup_expr='icontains')

    category = filters.CharFilter(
        field_name="category", lookup_expr='icontains')

    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')

    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    min_quantity = filters.NumberFilter(
        field_name='quantity', lookup_expr='gte')

    max_quantity = filters.NumberFilter(
        field_name='quantity', lookup_expr='lte')

    created_at = filters.DateFilter(
        field_name="created_at", lookup_expr='date')

    class Meta:
        model = Products
        fields = ['name', 'brand', 'category', 'min_price',
                  'max_price', 'min_quantity', 'max_quantity', 'created_at']
