from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from core.views import home


def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product/product.html', {'product': product})


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = {}
    context['form'] = ProductForm()
    return render(request, 'product/form.html', context)


def product_edit(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product', id=product.id)

    context = {}
    context["form"] = ProductForm(instance=product)
    return render(request, "product/form.html", context)
