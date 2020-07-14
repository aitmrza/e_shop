from django.shortcuts import redirect, render

from core.views import home
from .forms import ProductForm
from .models import Product


def product(request, id):
    """Страница товара с его полным описанием"""
    product = Product.objects.get(id=id)
    return render(request, 'product/product.html', {'product': product})


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {}
            context['products'] = Product.objects.filter(availability=True)
            context['product_added'] = 'Товар опубликован'
            return render(request, 'core/home.html', context)
    context = {}
    context['form'] = ProductForm()
    return render(request, 'product/form.html', context)


def product_edit(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            context = {}
            context['product'] = Product.objects.get(id=id)
            context['product_edit'] = 'Товар отредактирован'
            return render(request, 'product/product.html', context)

    context = {}
    context["form"] = ProductForm(instance=product)
    return render(request, "product/form.html", context)

def product_delete(request, id):
    Product.objects.get(id=id).delete()
    return redirect(home)
