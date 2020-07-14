from django.urls import path

from .views import *

urlpatterns = [
    path('<int:id>/', product, name='product'),
    path('add', product_add, name='product-add'),
    path('edit/<int:id>', product_edit, name='product-edit'),
    path('delete/<int:id>', product_delete, name='product-delete')
]
