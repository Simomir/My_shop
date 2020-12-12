from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'price', 'image')
    list_filter = ('name', 'user', 'price')
    search_fields = ('name', 'description')
