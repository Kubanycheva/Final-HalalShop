from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from .serializers import ChangePasswordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import VerifyResetCodeSerializer


@api_view(['POST'])
def verify_reset_code(request):
    serializer = VerifyResetCodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Пароль успешно сброшен.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'PUT':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(generics.CreateAPIView): # Регистрация для обычных пользователей
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='refresh_token'),
            },
            required=['refresh_token']
        ),
    )
    def post(self, request):
        serializer = UserLogoutSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'detail': 'Вы успешно вышли.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SalesmanViewSet(viewsets.ModelViewSet):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class MeatsProductViewSet(viewsets.ModelViewSet):
    queryset = MeatsProduct.objects.all()
    serializer_class = MeatsProductSerializer


class MeatsProductDetailAPIVIew(generics.RetrieveAPIView):
    queryset = MeatsProduct.objects.all()
    serializer_class = MeatsProductCardSerializer


class BirdProductViewSet(viewsets.ModelViewSet):
    queryset = BirdProduct.objects.all()
    serializer_class = BirdProductSerializer


class BirdProductDetailAPIVIew(generics.RetrieveAPIView):
    queryset = BirdProduct.objects.all()
    serializer_class = BirdProductCardSerializer


class FishProductViewSet(viewsets.ModelViewSet):
    queryset = FishProduct.objects.all()
    serializer_class = FishProductSerializer


class FishProductDetailAPIView(generics.RetrieveAPIView):
    queryset = FishProduct.objects.all()
    serializer_class = FishProductCardSerializer


class FrozenProductViewSet(viewsets.ModelViewSet):
    queryset = FrozenProduct.objects.all()
    serializer_class = FrozenProductSerializer


class FrozenProductDetailAPIView(generics.RetrieveAPIView):
    queryset = FrozenProduct.objects.all()
    serializer_class = FrozenProductCardSerializer


class DairyViewSet(viewsets.ModelViewSet):
    queryset = Dairy.objects.all()
    serializer_class = DairySerializer


class DairyDetailAPIView(generics.RetrieveAPIView):
    queryset = Dairy.objects.all()
    serializer_class = DairyCardSerializer


class BakeryProductViewSet(viewsets.ModelViewSet):
    queryset = BakeryProduct.objects.all()
    serializer_class = BakeryProductSerializer


class BakeryProductDetailAPIView(generics.RetrieveAPIView):
    queryset = BakeryProduct.objects.all()
    serializer_class = BakeryProductCardSerializer


class ConfectioneryProductViewSet(viewsets.ModelViewSet):
    queryset = ConfectioneryProduct.objects.all()
    serializer_class = ConfectioneryProductSerializer


class ConfectioneryProductDetailAPIView(generics.RetrieveAPIView):
    queryset = ConfectioneryProduct.objects.all()
    serializer_class = ConfectioneryProductCardSerializer


class ReadyMealViewSet(viewsets.ModelViewSet):
    queryset = ReadyMeal.objects.all()
    serializer_class = ReadyMealSerializer


class ReadyMealDetailAPIView(generics.RetrieveAPIView):
    queryset = ReadyMeal.objects.all()
    serializer_class = ReadyMealCardSerializer


class GrocerProductViewSet(viewsets.ModelViewSet):
    queryset = GrocerProduct.objects.all()
    serializer_class = GrocerProductSerializer


class GrocerDetailAPIView(generics.RetrieveAPIView):
    queryset = GrocerProduct.objects.all()
    serializer_class = GrocerProductCardSerializer


class DrinkProductViewSet(viewsets.ModelViewSet):
    queryset = DrinkProduct.objects.all()
    serializer_class = DrinkProductSerializer


class DrinkProductDetailAPIView(generics.RetrieveAPIView):
    queryset = DrinkProduct.objects.all()
    serializer_class = DrinkProductCardSerializer


class BabyProductViewSet(viewsets.ModelViewSet):
    queryset = BabyProduct.objects.all()
    serializer_class = BabyProductSerializer


class BabyProductDetailAPIVIew(generics.RetrieveAPIView):
    queryset = BabyProduct.objects.all()
    serializer_class = BabyProductCardSerializer


class HomeProductViewSet(viewsets.ModelViewSet):
    queryset = HomeProduct.objects.all()
    serializer_class = HomeProductSerializer


class HomeProductDetailAPIVIew(generics.RetrieveAPIView):
    queryset = HomeProduct.objects.all()
    serializer_class = HomeProductCardSerializer


class HealthBeautyViewSet(viewsets.ModelViewSet):
    queryset = HealthBeauty.objects.all()
    serializer_class = HealthBeautySerializer


class HealthBeautyDetailAPIVIew(generics.RetrieveAPIView):
    queryset = HealthBeauty.objects.all()
    serializer_class = HealthBeautyCardSerializer


class VitaminsViewSet(viewsets.ModelViewSet):
    queryset = Vitamins.objects.all()
    serializer_class = VitaminsSerializer


class VitaminsDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Vitamins.objects.all()
    serializer_class = VitaminsCardSerializer


class PharmaceuticalViewSet(viewsets.ModelViewSet):
    queryset = Pharmaceutical.objects.all()
    serializer_class = PharmaceuticalSerializer


class PharmaceuticalDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Pharmaceutical.objects.all()
    serializer_class = PharmaceuticalCardSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer