from django.http import JsonResponse
from .models import Product, Warehouse

def get_product_info(request):
    products = Product.objects.all()
    result = []
    for product in products:
        product_info = {
            'product_name': product.name,
            'product_qty': product.quantity,
            'product_materials': []
        }
        product_materials = product.productmaterial_set.all()
        for product_material in product_materials:
            warehouse_info = {
                'warehouse_id': product_material.material.warehouse.id,
                'material_name': product_material.material.name,
                'qty': min(product_material.quantity, product_material.material.warehouse.remainder),
                'price': product_material.material.warehouse.price
            }
            product_info['product_materials'].append(warehouse_info)
        result.append(product_info)
    return JsonResponse({'result': result})
