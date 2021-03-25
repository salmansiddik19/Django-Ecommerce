from django.contrib import admin

from .models import Product, ProductRating


admin.site.register(Product)
admin.site.register(ProductRating)
