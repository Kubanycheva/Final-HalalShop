from rest_framework import viewsets, generics, status
from .serializers import *


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MeatsProductViewSet(generics.ListAPIView): # Мясные продукты
    queryset = MeatsProduct.objects.all()
    serializer_class = MeatsProductSerializer
