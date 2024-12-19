from django.contrib import admin

from product_module.models import Product, ProductColor, Brand, BuiltCountry

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(Brand)
admin.site.register(BuiltCountry)