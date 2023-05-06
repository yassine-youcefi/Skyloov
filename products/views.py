from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Products, Cart
from .filters import ProductsFilter
from .pagination import CustomPageNumber
from .serializers import GetProductsSerializer, GetCartSerializer, PostCartSerializer

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductsFilterView(generics.ListAPIView):
    """
        Search and filter products with (name, brand, price, quantity, rating, created_at)
    """
    serializer_class = GetProductsSerializer
    filter_class = ProductsFilter
    pagination_class = CustomPageNumber
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Products.objects.all()
        return self.filter_class(self.request.GET, queryset=queryset).qs



class GetCartListView(generics.ListAPIView):
    """
        List all the carts with the owner that make the request
    """
    
    serializer_class = GetCartSerializer
    pagination_class = CustomPageNumber
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        return get_list_or_404(Cart, owner=self.request.user)
    
    
class PostCartView(APIView):
    """
        Create cart instance view
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        
        data=request.data
        print(data)
        data.update({'owner': request.user.id})
        serializer = PostCartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            cart_data = GetCartSerializer(serializer.instance).data
            return Response(cart_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
