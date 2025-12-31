from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'category','low_stock')
    list_filter = ('available', 'category')
    search_fields = ('name',)
    list_editable = ('price', 'stock', 'available')
    list_per_page = 10
