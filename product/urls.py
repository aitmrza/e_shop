from django.urls import path
from .views import product


urlpatterns = [
    path('<int:id>/', product, name='product')
]