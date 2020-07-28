from django.db.models import Q
from django.shortcuts import render

from product.models import Product


def home(request):
    """Главная страница с каталогом товаров"""
    if 'key_word' in request.GET:
        key = request.GET.get('key_word')
        products = Product.objects.filter(
            Q(availability=True),
            Q(display=True),
            Q(name__icontains=key) |
            Q(category__name__icontains=key) |
            Q(description__icontains=key)
        )
        products.distinct()
    else:
        products = Product.objects.filter(availability=True, display=True)

    return render(request, 'core/home.html', {'products': products})
