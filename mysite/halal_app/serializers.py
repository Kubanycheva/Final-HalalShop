from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class MeatsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeatsProduct
        fields = ['id', 'meets_name']




