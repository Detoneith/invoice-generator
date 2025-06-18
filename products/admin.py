from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'expiry_date')
    list_filter = ('expiry_date',)
    search_fields = ('name',)