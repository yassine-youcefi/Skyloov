from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Products, Cart
from .filters import ProductsFilter
from .pagination import CustomPageNumber
from .serializers import GetProductsSerializer, GetCartSerializer, PostCartSerializer

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
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
        filter_queryset = self.filter_class(self.request.GET, queryset=queryset).qs
        
        sort = self.request.query_params.get('sort', None)
        if sort:
            try:
                filter_queryset = filter_queryset.order_by(sort)
            except:
                raise ValidationError({'detail': 'Invalid value for sort parameter.'})
                
                     
        return filter_queryset


class GetCartListView(generics.ListAPIView):
    """
        List all the carts with the owner that make the request
    """
    
    serializer_class = GetCartSerializer
    pagination_class = CustomPageNumber
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        return get_list_or_404(Cart, owner=self.request.user)
    
    
class CreateCartView(APIView):
    """
        Create cart instance view
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        
        data=request.data
        data.update({'owner': request.user.id})
        serializer = PostCartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            cart_data = GetCartSerializer(serializer.instance).data
            return Response(cart_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class CartView(APIView):
    """
        Cart view for get, update and delete cart instance, if the request.user is the owner
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

        
    def get(self, request, pk, format=None):
        cart = get_object_or_404(Cart, pk=pk, owner=request.user)
        serializer = GetCartSerializer(cart)
        return Response(serializer.data) 
    
    def put(self, request, pk, format=None):
        cart = get_object_or_404(Cart, pk=pk, owner=request.user)
        serializer = PostCartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cart_data = GetCartSerializer(serializer.instance).data
            return Response(cart_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        cart = get_object_or_404(Cart, pk=pk, owner=request.user)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            