from django.contrib.auth.models import User
from django.db import models
from mptt.models import TreeForeignKey


class Product(models.Model):
    name = models.CharField('Наименование товара', max_length=70)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='product',
        verbose_name='Продавец')
    category = TreeForeignKey(
        to='Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='product',
        verbose_name='Категория товара')
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
        upload_to='product_images',
        default="product_images/no_image.png")
    description = models.TextField('Описание', null=True, blank=True)
    price = models.DecimalField(
        'Цена',
        max_digits=11,
        decimal_places=0,
        default=0)
    bought = models.IntegerField('Куплено', default=0)
    availability = models.BooleanField('В наличии', default=True)
    display = models.BooleanField('Отображение', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
