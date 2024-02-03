from django.contrib import admin
from products.models import Product, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'desc', ('quantity', 'price'), 'image', 'category')
    search_fields = ('name',)
