from django.shortcuts import render
from product.models import Product

def home(request):
    products = Product.objects.filter(availability=True)
    return render(request, 'core/home.html', {'products': products})


def test(request):
    return HttpResponse('test page')
