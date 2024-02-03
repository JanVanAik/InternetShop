from django.shortcuts import render
from products.models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {
        'title': "GeekShop"
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context = {
        'title': "GeekShop - Продукты",
        'products': products,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)


