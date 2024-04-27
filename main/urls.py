from django.urls import path
from .views import ProductInfoAPIView

urlpatterns = [
    path("products-info/", 
         ProductInfoAPIView.as_view(), 
         name='product_info'
         )
]
