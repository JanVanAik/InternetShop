from django.shortcuts import render
from products.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    context = {
        'title': "GeekShop"
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 2)
    try:
        products_paginator = paginator.page(page)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)

    context = {
        'title': "GeekShop - Продукты",
        'products': products_paginator,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)


