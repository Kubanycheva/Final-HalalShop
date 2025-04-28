from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'category', CategoryViewSet)
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

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]
