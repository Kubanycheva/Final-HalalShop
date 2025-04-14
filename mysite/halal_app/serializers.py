from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MeatsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeatsProduct
        fields = '__all__'


class BirdProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdProduct
        fields = '__all__'


class FishProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishProduct
        fields = '__all__'


class FrozenProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrozenProduct
        fields = '__all__'


class DairySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = '__all__'


class BakeryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryProduct
        fields = '__all__'


class ConfectioneryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfectioneryProduct
        fields = '__all__'


class ReadyMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyMeal
        fields = '__all__'


class GrocerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrocerProduct
        fields = '__all__'


class DrinkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkProduct
        fields = '__all__'


class BabyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyProduct
        fields = '__all__'


class HomeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProduct
        fields = '__all__'


class HealthBeautySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthBeauty
        fields = '__all__'


class VitaminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamins
        fields = '__all__'


class PharmaceuticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmaceutical
        fields = '__all__'








