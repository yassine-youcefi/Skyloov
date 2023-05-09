from django.contrib import admin
from django.urls import path
from .views import (ProductsFilterView, GetCartListView,
                    CreateCartView, CartView, CartItemsView, ProductImageUploadView,)

urlpatterns = [
    path('search/', ProductsFilterView.as_view(), name="products-search"),
    path('<int:pk>/image_upload/', ProductImageUploadView.as_view(), name='product_image_upload'),
    path('cart/all/', GetCartListView.as_view(), name="carts-list"),
    path('cart/create/', CreateCartView.as_view(), name="create-cart"),
    path('cart/<int:pk>/', CartView.as_view(), name="cart"),
    path('cart/<int:pk>/items/', CartItemsView.as_view(), name="cart-items"),


]
