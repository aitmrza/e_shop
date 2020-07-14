from django.db.models import Q
from django.shortcuts import render

from product.models import Product


def home(request):
    """Главная страница с каталогом товаров"""
    if 'key_word' in request.GET:
        key = request.GET.get('key_word')
        products = Product.objects.filter(
            Q(availability=True),
            Q(name__contains=key) | Q(category__name__contains=key) |
            Q(description__contains=key)
        )
        products.distinct()
    else:
        products = Product.objects.filter(availability=True)
    return render(request, 'core/home.html', {'products': products})


def test(request):
    return HttpResponse('test page')
