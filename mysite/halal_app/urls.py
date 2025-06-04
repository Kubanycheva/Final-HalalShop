from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()



urlpatterns = [
    path('', include(router.urls)),

    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('meats/', MeatsProductViewSet.as_view(), name='meats-list'),

]
