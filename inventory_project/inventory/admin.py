from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'product_status', 'created_date')
    list_filter = ('product_status',)
    search_fields = ('name',)

