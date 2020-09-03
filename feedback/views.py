from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .forms import FeedBackForm


@require_POST
def feedback(request):
    form = FeedBackForm(request.POST, request.FILES)
    if form.is_valid():
        feedback = form.save()
        if request.user.is_authenticated:
            feedback.user = request.user
            feedback = form.save()
        messages.info(request, 'Отзыв отправлен.')
        return redirect('home')
