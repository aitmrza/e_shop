from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    readonly_fields = ['user', 'bought', 'price', 'availability']
    list_display = [field.name for field in Product._meta.get_fields()[1:] if field.name != 'description']
    list_display_links = ('id', 'name')
    search_fields = ['name', 'description', 'user__username']
    list_filter = ['category', 'name']
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    model = Category
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Связанные продукты (Для этой конкретной категории)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Связанные продукты'
