from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

from product.models import Product


def home(request):
    """Главная страница с каталогом товаров"""
    if 'key_word' in request.GET:
        key = request.GET.get('key_word')
        products = Product.objects.filter(
            Q(availability=True),
            Q(name__icontains=key) |
            Q(category__name__icontains=key) |
            Q(description__icontains=key)
        )
        products.distinct()
    else:
        products = Product.objects.filter(availability=True)
    return render(request, 'core/home.html', {'products': products})


def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    if 'login' in request.POST:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(home)

    context = {}
    context['form'] = AuthenticationForm()
    return render(request, 'core/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect(home)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)

    context = {}
    context["form"] = RegistrationForm()
    return render(request, "core/registration.html", context)
