from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .models import *
from .serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SalesmanViewSet(viewsets.ModelViewSet):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MeatsProductViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = MeatsProductSerializer


class BirdProductViewSet(viewsets.ModelViewSet):
    queryset = BirdProduct.objects.all()
    serializer_class = BirdProductSerializer


class FishProductViewSet(viewsets.ModelViewSet):
    queryset = FishProduct.objects.all()
    serializer_class = FishProductSerializer


class FrozenProductViewSet(viewsets.ModelViewSet):
    queryset = FrozenProduct.objects.all()
    serializer_class = FrozenProductSerializer


class DairyViewSet(viewsets.ModelViewSet):
    queryset = Dairy.objects.all()
    serializer_class = DairySerializer


class BakeryProductViewSet(viewsets.ModelViewSet):
    queryset = BakeryProduct.objects.all()
    serializer_class = BakeryProductSerializer


class ConfectioneryProductViewSet(viewsets.ModelViewSet):
    queryset = ConfectioneryProduct.objects.all()
    serializer_class = ConfectioneryProductSerializer


class ReadyMealViewSet(viewsets.ModelViewSet):
    queryset = ReadyMeal.objects.all()
    serializer_class = ReadyMealSerializer


class GrocerProductViewSet(viewsets.ModelViewSet):
    queryset = GrocerProduct.objects.all()
    serializer_class = GrocerProductSerializer


class DrinkProductViewSet(viewsets.ModelViewSet):
    queryset = DrinkProduct.objects.all()
    serializer_class = DrinkProductSerializer


class BabyProductViewSet(viewsets.ModelViewSet):
    queryset = BabyProduct.objects.all()
    serializer_class = BabyProductSerializer


class HomeProductViewSet(viewsets.ModelViewSet):
    queryset = HomeProduct.objects.all()
    serializer_class = HomeProductSerializer


class HealthBeautyViewSet(viewsets.ModelViewSet):
    queryset = HealthBeauty.objects.all()
    serializer_class = HealthBeautySerializer


class VitaminsViewSet(viewsets.ModelViewSet):
    queryset = Vitamins.objects.all()
    serializer_class = VitaminsSerializer


class PharmaceuticalViewSet(viewsets.ModelViewSet):
    queryset = Pharmaceutical.objects.all()
    serializer_class = PharmaceuticalSerializer
