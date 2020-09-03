from django import forms
from .models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'email', 'topic', 'text', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Карл Штейн'}),
            'email': forms.TextInput(attrs={'placeholder': 'email@example.com'}),
            'topic': forms.TextInput(attrs={'placeholder': 'Быстрая доставка'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Пожалуйста, опишите свою идею как можно подробнее...'})
        }
