from django.urls import path
from .views import get_product_info

urlpatterns = [
    path("products/", get_product_info, name='product_info')
]
