from django.db import models

from product.models import Product


class Order(models.Model):
    receiver_name = models.CharField('Имя получателя', max_length=120)
    phone_number = models.CharField('Номер телефона', max_length=55)


class ProductInOrder(models.Model):
    order = models.ForeignKey(
        to=Order,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='product_in_order',
        verbose_name='Заказ')
    product = models.ForeignKey(
        to=Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='product_in_order',
        verbose_name='Товар')
    order_date = models.DateTimeField(
        'Дата заказа', auto_now_add=True, null=True)
