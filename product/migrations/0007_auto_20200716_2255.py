# Generated by Django 3.0.8 on 2020-07-16 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to=settings.AUTH_USER_MODEL, verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='bought',
            field=models.IntegerField(default=0, verbose_name='Куплено'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product.Category', verbose_name='Категория товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='product_images/no_image.png', null=True, upload_to='product_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=70, verbose_name='Наименование товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=11, verbose_name='Цена'),
        ),
    ]
