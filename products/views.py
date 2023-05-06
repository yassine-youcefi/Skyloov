from django.shortcuts import render
from .models import Products
from rest_framework import generics
from .filters import ProductsFilter
from .pagination import CustomPageNumber
from .serializers import GetProductsSerializer
from rest_framework.permissions import IsAuthenticated


class ProductsFilterView(generics.ListAPIView):
    serializer_class = GetProductsSerializer
    filter_class = ProductsFilter
    pagination_class = CustomPageNumber
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Products.objects.all()
        return self.filter_class(self.request.GET, queryset=queryset).qs
