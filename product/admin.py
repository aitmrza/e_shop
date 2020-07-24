from django.contrib import admin

from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    readonly_fields = ['user', 'bought', 'price', 'availability']
    list_display = [field.name for field in Product._meta.get_fields() if field.name != 'description']
    list_display_links = ('id', 'name')
    search_fields = ['name', 'description', 'user__username']
    list_filter = ['category', 'name']
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = [field.name for field in Category._meta.get_fields()[1:]]
    list_editable = ('name',)
    search_fields = ['name']