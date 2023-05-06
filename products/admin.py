from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Products._meta.get_fields()]
    search_fields = ['name', 'brand']
