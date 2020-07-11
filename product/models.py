from django.db import models


class Product(models.Model):
    name = models.CharField('Наименование', max_length=30)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.SET_NULL,
        related_name='product',
        null=True,
        blank=True,
        verbose_name='Категория')
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
        upload_to='product_images')
    description = models.TextField('Описание', null=True, blank=True)
    price = models.IntegerField('Цена', default=0)
    bought = models.IntegerField('Куплено')
    availability = models.BooleanField('В наличии', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    name = models.CharField('Название', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
