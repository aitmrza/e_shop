from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', blank=True)
    price = models.FloatField('Цена')
    number_purchases = models.IntegerField('Кол-во покупок', default=0)
    availability = models.BooleanField('В наличии', default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'