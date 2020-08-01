from django.contrib import admin

from .models import *


class ProductInOrderInline(admin.StackedInline):
    model = ProductInOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['receiver_name', 'phone_number', 'get_product_count']
    inlines = [ProductInOrderInline]

    def get_product_count(self, obj):
        return obj.product_in_order.count()


@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    model = ProductInOrder
    list_display = ('order', 'product', 'order_date')
    readonly_fields = ('order', 'product', 'order_date')
