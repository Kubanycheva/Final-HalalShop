from rest_framework import generics
from .models import Category, Product
from .serializers import (
    CategoryDetailSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    CategorySimpleSerializer
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySimpleSerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'pk'


class ProductListByCategoryView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'



