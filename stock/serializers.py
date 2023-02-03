from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "product_count")

    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = '__all__'


class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "product_count", "products")

    def get_product_count(self, obj):
        return Product.objects.filter(category_id=obj.id).count()