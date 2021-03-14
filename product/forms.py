from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'product_name',
                  'product_price', 'product_image')


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'product_name',
                  'product_price', 'product_image')
