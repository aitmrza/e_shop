from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProductForm
from .models import Product
from core.views import home


def product(request, id):
    """Страница товара с его полным описанием"""
    product = Product.objects.get(id=id)
    return render(request, 'product/product.html', {'product': product})


@login_required(login_url='login')
def product_add(request):
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = request.user
            new_product.save()
            context['products'] = Product.objects.filter(availability=True)
            context['product_added'] = 'Товар опубликован.'
            return render(request, 'core/home.html', context)

    context['form'] = ProductForm()
    return render(request, 'product/form.html', context)


@login_required(login_url='home')
def product_edit(request, id):
    product = Product.objects.get(id=id)
    context = {}
    if request.user != product.user:
        return redirect(home)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            context['product'] = Product.objects.get(id=id)
            context['product_edit'] = 'Товар отредактирован.'
            return render(request, 'product/product.html', context)

    context["form"] = ProductForm(instance=product)
    return render(request, 'product/form.html', context)


@login_required(login_url='home')
def product_delete(request, id):
    product = Product.objects.get(id=id)
    if request.user != product.user:
        return redirect(home)

    context = {}
    context['product'] = Product.objects.get(id=id).delete()
    context['products'] = Product.objects.filter(availability=True)
    context['product_delete'] = 'Товар удален.'
    return render(request, 'core/home.html', context)
