from django.contrib import auth, messages
from django.shortcuts import redirect, render

from core.forms import RegistrationForm
from product.models import Product


def profile(request, id):
    """Личный кабинет персонального пользователя"""
    context = {}
    context['user'] = auth.models.User.objects.get(id=id)
    context['products'] = Product.objects.filter(user=context['user'])
    return render(request, 'core/profile.html', context)


def login(request):
    """Авторизация пользователя"""
    if request.user.is_authenticated:
        return redirect('home')
    if 'login' in request.POST:
        form = auth.forms.AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home')

    context = {}
    context['form'] = auth.forms.AuthenticationForm()
    return render(request, 'core/login.html', context)


def logout(request):
    """Выход из личного кабинета"""
    auth.logout(request)
    return redirect('home')


def registration(request):
    """Форма регистрации"""
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login)

    context = {}
    context['form'] = RegistrationForm()
    return render(request, 'core/registration.html', context)


@auth.decorators.login_required
def password_change(request):
    """Изменение своего пароля пользователем"""
    user = request.user
    if request.user.id != user.id:
        return redirect('home')
    if request.method == 'POST':
        form = auth.forms.PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request, form.user)
            messages.success(request, 'Ваш пароль был успешно изменен.')
            return redirect('profile', id=user.id)
    else:
        form = auth.forms.PasswordChangeForm(user=request.user)

    return render(request, 'core/password_change_form.html', {'form': form})
