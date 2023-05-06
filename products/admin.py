from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'price', 'rating', 'created_at']
    search_fields = ['name', 'brand']
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'total','created_at', 'updated_at']
    search_fields = ['item__name']    
