from django.db import models


class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name
