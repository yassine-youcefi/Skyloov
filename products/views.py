from django.shortcuts import render
from rest_framework import status, permissions, generics
from .models import Products
from .filters import ProductsFilter
from .pagination import CustomPageNumber
from .serializers import GetProductsSerializer

class ProductsFilterView(generics.ListAPIView):
    serializer_class = GetProductsSerializer
    filter_class = ProductsFilter
    pagination_class = CustomPageNumber


    def get_queryset(self):
        queryset = Products.objects.all()
        return self.filter_class(self.request.GET, queryset=queryset).qs
    
    
    
    
        # if (self.request.query_params.get("min_price")) and (self.request.query_params.get("max_price")):
        #     min_price = self.request.query_params.get("min_price")
        #     max_price = self.request.query_params.get("max_price")

        #     try:
        #         queryset = queryset.filter(
        #             price__range=(min_price, max_price)).distinct()

        #         return products

        #     except ObjectDoesNotExist:
        #         raise Http404
        # elif self.request.query_params.get("category"):
        #     print('ok')
                

        # return queryset