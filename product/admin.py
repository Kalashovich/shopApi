from django.contrib import admin

from product.models import Product, NewProduct, Category

admin.site.register(Product)
admin.site.register(NewProduct)
admin.site.register(Category)

