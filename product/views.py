from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.filter(availability=True)
    return render(request, 'product/products.html', {'products': products})
