from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'salesman', SalesmanViewSet)
router.register(r'buyer', BuyerViewSet)
router.register(r'meats', MeatsProductViewSet)
router.register(r'bird', BirdProductViewSet)
router.register(r'fish', FishProductViewSet)
router.register(r'frozen', FrozenProductViewSet)
router.register(r'dairy', DairyViewSet)
router.register(r'bakery', BakeryProductViewSet)
router.register(r'confectionery', ConfectioneryProductViewSet)
router.register(r'ready_meal', ReadyMealViewSet)
router.register(r'grocer', GrocerProductViewSet)
router.register(r'drink', DrinkProductViewSet)
router.register(r'baby', BabyProductViewSet)
router.register(r'home', HomeProductViewSet)
router.register(r'health', HealthBeautyViewSet)
router.register(r'vitamin', VitaminsViewSet)
router.register(r'pharmaceutical', PharmaceuticalViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('user-register/', UserRegisterView.as_view(), name='user-register'),
    path('user-login/', UserLoginView.as_view(), name='user-login'),
    path('user-logout/', UserLogoutView.as_view(), name='user-logout'),


    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category-detail'),
    path('category/product/<int:pk>/', BabyProductDetailAPIVIew.as_view(), name='category-detail'),
    path('category/meats/<int:pk>/', MeatsProductDetailAPIVIew.as_view(), name='category-detail'),
    path('category/bird/<int:pk>/', BirdProductDetailAPIVIew.as_view(), name='category-detail'),
    path('category/fish/<int:pk>/', FishProductDetailAPIView.as_view(), name='category-detail'),
    path('category/frozen/<int:pk>/', FrozenProductDetailAPIView.as_view(), name='category-detail'),
    path('category/dairy/<int:pk>/', DairyDetailAPIView.as_view(), name='category-detail'),
    path('category/bakery/<int:pk>/', BakeryProductDetailAPIView.as_view(), name='category-detail'),
    path('category/conditer/<int:pk>/', ConfectioneryProductDetailAPIView.as_view(), name='category-detail'),
    path('category/ready_meal/<int:pk>/', ReadyMealDetailAPIView.as_view(), name='category-detail'),
    path('category/grocer/<int:pk>/', GrocerDetailAPIView.as_view(), name='category-detail'),
    path('category/drink/<int:pk>/', DrinkProductDetailAPIView.as_view(), name='category-detail'),
    path('category/baby/<int:pk>/', BabyProductDetailAPIVIew.as_view(), name='category-detail'),
    path('category/home/<int:pk>/', HomeProductDetailAPIVIew.as_view(), name='category-detail'),
    path('category/vitamin/<int:pk>/', VitaminsDetailAPIVIew.as_view(), name='category-detail'),
    path('category/pharmacy/<int:pk>/', PharmaceuticalDetailAPIVIew.as_view(), name='category-detail'),

]
