from django.contrib import admin
from django.urls import path
from .views import ProductsFilterView

urlpatterns = [
    path('search/', ProductsFilterView.as_view(), name="products-search"),
]
