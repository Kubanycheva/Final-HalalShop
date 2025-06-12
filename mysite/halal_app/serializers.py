from rest_framework import serializers
from .models import Category, Brand, Product, ProductImage, Customer, Order, OrderItem, Review


class RecursiveCategorySerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = CategoryDetailSerializer(value, context=self.context)
        return serializer.data


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    subcategories = RecursiveCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'subcategories']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductListSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'weight', 'images']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"
        
    





