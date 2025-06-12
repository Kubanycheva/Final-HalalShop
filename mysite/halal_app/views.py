from rest_framework import generics, viewsets
from .models import Category, Product, Save, SaveItem, Cart, CartItem, Customer
from .serializers import (
    CategoryDetailSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    CategorySimpleSerializer,
    SaveSerializer,
    SaveItemSerializer,
    SaveItemListSerializer,
    CartSerializer,
    CartItemSerializer,
    CartItemListSerializer,
    CustomerSerializer
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



#
# class MeatsProductViewSet(generics.ListAPIView): # Мясные продукты
#     queryset = MeatsProduct.objects.all()
#     serializer_class = MeatsProductSerializer


class SaveViewSet(viewsets.ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer


class SaveItemCreateApiView(generics.CreateAPIView):
    serializer_class = SaveItemSerializer


class SaveItemListApiView(generics.ListAPIView):
    queryset = SaveItem.objects.all()
    serializer_class = SaveItemListSerializer


class SaveItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaveItem.objects.all()
    serializer_class = SaveItemListSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemCreateAPIView(generics.CreateAPIView):
    serializer_class = CartItemSerializer


class CartItemListApiView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer


class CartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer


class CartItemStatusListApiView(generics.ListAPIView):
    queryset = CartItem.objects.filter(status='в пути')
    serializer_class = CartItemListSerializer


class CartItemStatusDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.filter(status='в пути')
    serializer_class = CartItemDetailAPIView


class CustomerListApiView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
