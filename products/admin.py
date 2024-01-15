from django.contrib import admin

from products.models import ProductCategory, Product, Rate

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Rate)