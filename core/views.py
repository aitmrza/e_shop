from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render

from product.models import Product
from .forms import RegistrationForm


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
    """Авторизация пользователя"""
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
    """Выход из личного кабинета"""
    auth.logout(request)
    return redirect(home)


def registration(request):
    """Форма регистрации"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)

    context = {}
    context['form'] = RegistrationForm()
    return render(request, 'core/registration.html', context)


@login_required(login_url='login')
def profile(request, pk):
    """Личный кабинет персонального пользователя"""
    context = {}
    context['user'] = User.objects.get(id=pk)
    context['products'] = Product.objects.filter(user=context['user'])
    return render(request, 'core/profile.html', context)


def sellers(request):
    sellers = User.objects.exclude(product=None)
    return render(request, "core/sellers.html", {"sellers": sellers})
