from ast import mod
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.code}"


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=0)


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    remainder = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.material} - {self.remainder} - {self.price}"
