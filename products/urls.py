from django.contrib import admin
from django.urls import path
from .views import ProductsFilterView, GetCartListView, PostCartView

urlpatterns = [
    path('search/', ProductsFilterView.as_view(), name="products-search"),
    path('cart/all/', GetCartListView.as_view(), name="carts-list"),
    path('cart/create/', PostCartView.as_view(), name="create-cart"),

]
