from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    product = models.ManyToManyField(
        'Product',
        related_name='products',
        verbose_name='Товар')
    quantity = models.PositiveIntegerField('Количество штук', default=1)
    delivery_address = models.CharField('Адрес доставки', max_length=120)
    delivery_date = models.DateField('Дата доставки')
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='order',
        verbose_name='Заказчик')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
