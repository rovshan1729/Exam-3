from rest_framework import serializers
from .models import Product, Material, Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'id',
            'material', 
            'remainder', 
            'price'
            ]


class ProductSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'name', 
            'warehouse',
            ]
