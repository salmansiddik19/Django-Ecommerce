from rest_framework import serializers
from .models import Product, ProductRating
from user.models import User
from rest_framework.response import Response


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = '__all__'
