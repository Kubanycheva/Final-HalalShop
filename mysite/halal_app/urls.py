from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'salesman', SalesmanViewSet)
router.register(r'buyer', BuyerViewSet)



urlpatterns = [
    path('', include(router.urls)),

    path('user-register/', UserRegisterView.as_view(), name='user-register'),
    path('user-login/', UserLoginView.as_view(), name='user-login'),
    path('user-logout/', UserLogoutView.as_view(), name='user-logout'),
    path('user/me', UserProfileSimpleViewSet.as_view(), name='user-logout'),


    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


    path('category/', CategoryListAPIView.as_view(), name='category-list'),

    path('category/meats/', MeatsProductViewSet.as_view(), name='meats-lisy'),
    path('category/meats/<int:pk>/', MeatsProductCardViewSet.as_view(), name='meats-card'),
    path('category/meats/<int:pk>/product/', MeatsProductCardDetailViewSet.as_view(), name='meats-detail'),

    path('category/bird/', BirdProductViewSet.as_view(), name='bird-list'),
    path('category/bird/<int:pk>/', BirdProductCardViewSet.as_view(), name='bird-card'),
    path('category/bird/<int:pk>/product/', BirdProductCardDetailViewSet.as_view(), name='bird-detail'),

    path('category/fish/', FishProductViewSet.as_view(), name='fish-list'),
    path('category/fish/<int:pk>/', FishProductCardViewSet.as_view(), name='fish-card'),
    path('category/fish/<int:pk>/product/', FishProductCardDetailViewSet.as_view(), name='fish-detail'),

    path('category/frozen/', FrozenProductViewSet.as_view(), name='frozen-list'),
    path('category/frozen/<int:pk>/', FrozenProductCardViewSet.as_view(), name='frozen-card'),
    path('category/frozen/<int:pk>/product/', FrozenProductCardDetailViewSet.as_view(), name='frozen-detail'),

    path('category/dairy/', DairyViewSet.as_view(), name='dairy-list'),
    path('category/dairy/<int:pk>/', DairyCardViewSet.as_view(), name='dairy-card'),
    path('category/dairy/<int:pk>/product/', DairyCardDetailViewSet.as_view(), name='dairy-detail'),

    path('category/bakery/', BakeryProductViewSet.as_view(), name='bakery-list'),
    path('category/bakery/<int:pk>/', BakeryProductCardViewSet.as_view(), name='bakery-card'),
    path('category/bakery/<int:pk>/product/', BakeryProductCardDetailViewSet.as_view(), name='bakery-detail'),

    path('category/conditer/', ConfectioneryProductViewSet.as_view(), name='conditer-list'),
    path('category/conditer/<int:pk>/', ConfectioneryProductCardViewSet.as_view(), name='conditer-card'),
    path('category/conditer/<int:pk>/product/', ConfectioneryProductCardDetailViewSet.as_view(), name='conditer-detail'),

    path('category/ready_meal/', ReadyMealViewSet.as_view(), name='ready_meal-list'),
    path('category/ready_meal/<int:pk>/', ReadyMealCardViewSet.as_view(), name='ready_meal-card'),
    path('category/ready_meal/<int:pk>/product/', ReadyMealCardDetailViewSet.as_view(), name='ready_meal-detail'),

    path('category/grocer/', GrocerProductViewSet.as_view(), name='grocer-list'),
    path('category/grocer/<int:pk>/', GrocerProductCardViewSet.as_view(), name='grocer-card'),
    path('category/grocer/<int:pk>/product/', GrocerProductCardDetailViewSet.as_view(), name='grocer-detail'),

    path('category/drink/', DrinkProductViewSet.as_view(), name='drink-list'),
    path('category/drink/<int:pk>/', DrinkProductCardViewSet.as_view(), name='drink-card'),
    path('category/drink/<int:pk>/product/', DrinkProductCardDetailViewSet.as_view(), name='drink-detail'),

    path('category/baby/', BabyProductViewSet.as_view(), name='baby-list'),
    path('category/baby/<int:pk>/', BabyProductCardViewSet.as_view(), name='baby-card'),
    path('category/baby/<int:pk>/product/', BabyProductCardDetailViewSet.as_view(), name='baby-detail'),

    path('category/home/', HomeProductViewSet.as_view(), name='home-list'),
    path('category/home/<int:pk>/', HomeProductCardViewSet.as_view(), name='home-card'),
    path('category/home/<int:pk>/product/', HomeProductCardDetailViewSet.as_view(), name='home-detail'),

    path('category/vitamin/', VitaminsViewSet.as_view(), name='vitamin-list'),
    path('category/vitamin/<int:pk>/', VitaminsCardViewSet.as_view(), name='vitamin-card'),
    path('category/vitamin/<int:pk>/product/', VitaminsCardDetailViewSet.as_view(), name='vitamin-detail'),

    path('category/pharmacy/', PharmaceuticalViewSet.as_view(), name='pharmacy-list'),
    path('category/pharmacy/<int:pk>/', PharmaceuticalCardViewSet.as_view(), name='pharmacy-card'),
    path('category/pharmacy/<int:pk>/product/', PharmaceuticalCardDetailViewSet.as_view(), name='pharmacy-detail'),

    path('category/health/', HealthBeautyViewSet.as_view(), name='health-list'),
    path('category/health/<int:pk>/', HealthBeautyCardViewSet.as_view(), name='health-card'),
    path('category/health/<int:pk>/product/', HealthBeautyCardDetailViewSet.as_view(), name='health-detail'),


]
