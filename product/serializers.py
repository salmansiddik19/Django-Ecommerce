from rest_framework import serializers
from .models import Product, ProductRating
from user.models import User
from rest_framework.response import Response


class ProductRatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductRating
        fields = ('id', 'user', 'product', 'rating', 'update_count')
