from django.template.defaultfilters import first
from rest_framework import serializers
from .models import Category, Brand, Product, ProductImage, Customer, Order, OrderItem, Review


class RecursiveCategorySerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = CategoryDetailSerializer(value, context=self.context)
        return serializer.data


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image']


class CategoryDetailSerializer(serializers.ModelSerializer):
    subcategories = RecursiveCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image', 'subcategories']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductListSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'weight', 'images']


    def get_image(self, obj):
        image = obj.images.first()
        return image.image.url if image and image.image else None


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    images = ProductImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = "__all__"





