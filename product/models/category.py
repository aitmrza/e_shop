from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
