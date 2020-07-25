from django.contrib.auth.models import User
from django.shortcuts import render


def sellers(request):
    """Список продавцов"""
    sellers = User.objects.exclude(product=None)
    return render(request, "core/sellers.html", {"sellers": sellers})
