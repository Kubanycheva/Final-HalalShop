from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
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
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
]