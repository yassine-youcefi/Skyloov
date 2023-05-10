from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404

import multiprocessing

from .tasks import products_tasks
from .models import Products, Cart
from .filters import ProductsFilter
from .pagination import CustomPageNumber
from .serializers import (GetProductsSerializer, GetCartSerializer, PostCartSerializer,
                          CartItemsSerializer, CreateProductSerializer, UpdateProductImageSerializer)

from rest_framework import generics, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


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
        filter_queryset = self.filter_class(
            self.request.GET, queryset=queryset).qs

        sort = self.request.query_params.get('sort', None)
        if sort:
            try:
                filter_queryset = filter_queryset.order_by(sort)
            except:
                raise ValidationError(
                    {'detail': 'Invalid value for sort parameter.'})

        return filter_queryset


class CreateProductView(generics.CreateAPIView):
    """
        Create product instance, ['name', 'brand', 'description', 'category', 'price', 'quantity', 'rating']
    """
    serializer_class = CreateProductSerializer
    queryset = Products.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            serializer = GetProductsSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductImageUploadView(generics.UpdateAPIView):
    """
        Update product images , ['image']
    """
    model = Products
    fields = ['image']
    queryset = Products.objects.all()
    serializer_class = UpdateProductImageSerializer
    swagger_fake_view = True
    
    

    def put(self, request, *args, **kwargs):
        if 'image' not in request.FILES:
            return Response({'error': 'No image file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        product = self.get_object()

        serializer = self.get_serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()

            # products_tasks.product_media_task.delay(product.id)
            process = multiprocessing.Process(target=self.run_celery_task, args=(product.id,))
            process.start()
            process.join()
            return Response({'success': 'Image uploaded successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def run_celery_task(self, product_id):
        products_tasks.product_media_task.delay(product_id)


class GetCartListView(generics.ListAPIView):
    """
        List all the carts with the owner that make the request
    """

    serializer_class = GetCartSerializer
    pagination_class = CustomPageNumber
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user)


class CreateCartView(generics.CreateAPIView):
    """
    Create cart instance view
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostCartSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        context = super().get_serializer_context()
        context['owner'] = self.request.user
        return context


class CartView(generics.RetrieveDestroyAPIView):
    """
        Cart view for get and delete cart instance, if the request.user is the owner
    """
    permission_classes = [IsAuthenticated]
    serializer_class = GetCartSerializer
    queryset = Cart.objects.all()

    def get_object(self):
        return get_object_or_404(Cart, pk=self.kwargs['pk'], owner=self.request.user)


class CartItemsView(generics.RetrieveUpdateDestroyAPIView):
    """
        Cart items view for update and delete items in cart instance,
        if the request.user is the owner
    """
    serializer_class = CartItemsSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Cart, pk=self.kwargs['pk'], owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        """
        Remove one or more items from the cart
        """
        cart = self.get_object()
        items = request.data.get("items", [])

        if not isinstance(items, list):
            return Response(
                {"items": ["Items must be a list"]},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Remove each item from the cart
        for item_id in items:
            try:
                product = Products.objects.get(id=item_id)
                cart.remove_product(product)
            except product.DoesNotExist:
                pass  # Ignore items that do not exist

        # Serialize the updated cart and return a response
        serializer = self.get_serializer(cart)
        return Response(serializer.data)
