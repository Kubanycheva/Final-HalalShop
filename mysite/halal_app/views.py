from rest_framework.filters import OrderingFilter,  SearchFilter
from rest_framework import generics, filters
from .models import Category, Product
from .serializers import (
    CategoryDetailSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    CategorySimpleSerializer
)
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySimpleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category_name', 'parent__category_name']
    search_fields = ['category_name', 'parent__category_name']
    ordering_fields = ['category_name', 'parent__category_name']



class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category_name', 'parent__category_name']
    search_fields = ['category_name', 'parent__category_name']
    ordering_fields = ['category_name', 'parent__category_name']



class ProductListByCategoryView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['brand__brand_name', 'price']
    search_fields = ['product_name', 'brand__brand_name', 'category__category_name']
    ordering_fields = ['product_name', 'price', 'created_at']

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)


    # def get_serializer_class(self):
    #     if self.request.parser_context['view'].action == 'retrieve':
    #         return ProductDetailSerializer
    #     return ProductListSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['product_name', 'brand__brand_name']
    ordering_fields = ['product_name', 'price']




