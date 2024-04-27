from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouse

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'id',
            'material', 
            'remainder', 
            'price'
            ]

class ProductMaterialSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(many=True, read_only=True)
    class Meta:
        model = ProductMaterial
        fields = [
            'material', 
            'quantity', 
            'warehouse'
            ]

class ProductSerializer(serializers.ModelSerializer):
    product_materials = ProductMaterialSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'name', 
            'product_materials'
            ]
