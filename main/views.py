from rest_framework import generics
from rest_framework.response import Response
from .models import Product, Warehouse
from .serializers import ProductSerializer


class ProductInfoAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        for product in products:
            product_materials = product.productmaterial_set.all()
            for product_material in product_materials:
                product_material.quantity = min(product_material.quantity, product_material.material.warehouse.remainder)
        return products

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'result': serializer.data})
