from django.db import models
from user.models import User


class Product(models.Model):
    product_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    product_title = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name


class ProductRating(models.Model):
    CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=CHOICES, default=3)

    def __str__(self):
        return str(self.id) + " " + "|" + " Rating:" + str(self.rating)
