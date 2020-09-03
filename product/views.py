from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ProductForm
from .models import Product, Category


def product(request, id):
    """Страница товара с его полным описанием"""
    product = Product.objects.get(id=id)
    category_path = product.category.get_ancestors(include_self=True)
    return render(request, 'product/product.html', {'product': product, 'category_path': category_path})


@login_required(login_url='login')
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = request.user
            new_product.save()
            messages.success(request, 'Товар опубликован.')
            return redirect('home')
    return render(request, 'product/form.html', {'form': ProductForm()})


@login_required(login_url='home')
def product_edit(request, id):
    product = Product.objects.get(id=id)
    if request.user != product.user:
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар отредактирован.')
            return redirect('product', id=product.id)
    return render(request, 'product/form.html',
                  {'form': ProductForm(instance=product)})


@login_required(login_url='home')
def product_delete(request, id):
    product = Product.objects.get(id=id)
    if request.user != product.user:
        return redirect('home')
    product.delete()
    messages.error(request, 'Товар удален.')
    return redirect('home')


def category(request, pk):
    context = {}
    context['products'] = Product.objects.filter(
        category__id=pk,
        availability=True,
        display=True)
    context['category_pk'] = pk
    return render(request, 'core/home.html', context)

