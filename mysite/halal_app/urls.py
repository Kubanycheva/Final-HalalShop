from django.urls import path, include
from .views import *
from rest_framework import routers
from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    ProductListByCategoryView,
    ProductDetailView
)

router = routers.SimpleRouter()

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),                  # без подкатегорий
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),     # с подкатегориями
    path('categories/<int:category_id>/products/', ProductListByCategoryView.as_view(), name='products-by-category'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

