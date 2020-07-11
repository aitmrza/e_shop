from django.shortcuts import render
from .models import Product

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product/product.html', {'product': product})
