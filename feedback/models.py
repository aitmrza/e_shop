from django.db import models
from django.contrib.auth.models import User

class FeedBack(models.Model):
    name = models.CharField('Ваше имя', max_length=85, null=True, blank=True)
    email = models.EmailField('Ваша электронная почта')
    topic = models.CharField('Тема', max_length=55)
    text = models.TextField('Подробнее')
    image = models.ImageField('Приложить фотографию (рекомендуется)', upload_to='feedback' , null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField('Дата обращения', auto_now_add=True)

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'отзывы'
