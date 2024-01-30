from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse

from products.models import Product
from basket.models import Basket


# Create your views here.
def basket_add(request, product_id):
    user = request.user
    product = Product.objects.filter(id=product_id)
    baskets = Basket.objects.filter(user=user, product=product)
    if not baskets:
        Basket.objects.create(user=user, product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket = baskets.first()
        basket.quantity +=1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])



def basket_remove(request, id):
    basket = Basket.objects.filter(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
