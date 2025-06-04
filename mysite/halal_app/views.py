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
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


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


class UserRegisterView(generics.CreateAPIView):
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


class UserProfileSimpleViewSet(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class SalesmanViewSet(viewsets.ModelViewSet):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class MeatsProductViewSet(generics.ListAPIView): # Мясные продукты
    queryset = MeatsProduct.objects.all()
    serializer_class = MeatsProductSerializer


class MeatsProductCardViewSet(generics.ListAPIView): # Мясные продукты
    queryset = MeatsProduct.objects.all()
    serializer_class = MeatsProductCardSerializer


class MeatsProductCardDetailViewSet(generics.RetrieveAPIView): # Мясные продукты
    queryset = MeatsProduct.objects.all()
    serializer_class = MeatsProductCardDetailSerializer


class BirdProductViewSet(generics.ListAPIView):
    queryset = BirdProduct.objects.all()
    serializer_class = BirdProductSerializer


class BirdProductCardViewSet(generics.ListAPIView):
    queryset = BirdProduct.objects.all()
    serializer_class = BirdProductCardSerializer


class BirdProductCardDetailViewSet(generics.RetrieveAPIView):
    queryset = BirdProduct.objects.all()
    serializer_class = BirdProductCardDetailSerializer


class FishProductViewSet(generics.ListAPIView):
    queryset = FishProduct.objects.all()
    serializer_class = FishProductSerializer


class FishProductCardViewSet(generics.ListAPIView):
    queryset = FishProduct.objects.all()
    serializer_class = FishProductCardSerializer


class FishProductCardDetailViewSet(generics.RetrieveAPIView):
    queryset = FishProduct.objects.all()
    serializer_class = FishProductCardDetailSerializer


class FrozenProductViewSet(generics.ListAPIView):
    queryset = FrozenProduct.objects.all()
    serializer_class = FrozenProductSerializer

class FrozenProductCardViewSet(generics.ListAPIView):
    queryset = FrozenProduct.objects.all()
    serializer_class = FrozenProductCardSerializer


class FrozenProductCardDetailViewSet(generics.RetrieveAPIView):
    queryset = FrozenProduct.objects.all()
    serializer_class = FrozenProductCardDetailSerializer



class DairyViewSet(generics.ListAPIView):
    queryset = Dairy.objects.all()
    serializer_class = DairySerializer


class DairyCardViewSet(generics.ListAPIView):
    queryset = Dairy.objects.all()
    serializer_class = DairyCardSerializer


class DairyCardDetailViewSet(generics.RetrieveAPIView):
    queryset = Dairy.objects.all()
    serializer_class = DairyCardDetailSerializer


class BakeryProductViewSet(generics.ListAPIView):
    queryset = BakeryProduct.objects.all()
    serializer_class = BakeryProductSerializer


class BakeryProductCardViewSet(generics.ListAPIView):
    queryset = BakeryProduct.objects.all()
    serializer_class = BakeryProductCardSerializer

class BakeryProductCardDetailViewSet(generics.RetrieveAPIView):
    queryset = BakeryProduct.objects.all()
    serializer_class = BakeryProductCardDetailSerializer

class ConfectioneryProductViewSet(generics.ListAPIView):
    queryset = ConfectioneryProduct.objects.all()
    serializer_class = ConfectioneryProductSerializer


class ConfectioneryProductCardViewSet(generics.ListAPIView):
    queryset = ConfectioneryProduct.objects.all()
    serializer_class = ConfectioneryProductCardSerializer


class ConfectioneryProductCardDetailViewSet(generics.RetrieveAPIView):
    queryset = ConfectioneryProduct.objects.all()
    serializer_class = ConfectioneryProductCardDetailSerializer

class ReadyMealViewSet(generics.ListAPIView):
    queryset = ReadyMeal.objects.all()
    serializer_class = ReadyMealSerializer

class ReadyMealCardViewSet(generics.ListAPIView):
    queryset = ReadyMeal.objects.all()
    serializer_class = ReadyMealCardSerializer

class ReadyMealCardDetailViewSet(generics.RetrieveAPIView):
    queryset = ReadyMeal.objects.all()
    serializer_class = ReadyMealCardDetailSerializer


class GrocerProductViewSet(generics.ListAPIView):
    queryset = GrocerProduct.objects.all()
    serializer_class = GrocerProductSerializer

class GrocerProductCardViewSet(generics.ListAPIView):
    queryset = GrocerProduct.objects.all()
    serializer_class = GrocerProductCardSerializer


class GrocerProductCardDetailViewSet(generics.RetrieveAPIView):
    queryset = GrocerProduct.objects.all()
    serializer_class = GrocerProductCardDetailSerializer


class DrinkProductViewSet(generics.ListAPIView):
    queryset = DrinkProduct.objects.all()
    serializer_class = DrinkProductSerializer

class DrinkProductCardViewSet(generics.ListAPIView):
    queryset = DrinkProduct.objects.all()
    serializer_class = DrinkProductCardSerializer


class DrinkProductCardDetailViewSet(generics.RetrieveAPIView):
    queryset = DrinkProduct.objects.all()
    serializer_class = DrinkProductCardDetailSerializer


class BabyProductViewSet(generics.ListAPIView):
    queryset = BabyProduct.objects.all()
    serializer_class = BabyProductSerializer

class BabyProductCardViewSet(generics.ListAPIView):
    queryset = BabyProduct.objects.all()
    serializer_class = BabyProductCardSerializer

class BabyProductCardDetailViewSet(generics.RetrieveAPIView):
    queryset = BabyProduct.objects.all()
    serializer_class = BabyProductCardDetailSerializer


class HomeProductViewSet(generics.ListAPIView):
    queryset = HomeProduct.objects.all()
    serializer_class = HomeProductSerializer

class HomeProductCardViewSet(generics.ListAPIView):
    queryset = HomeProduct.objects.all()
    serializer_class = HomeProductCardSerializer

class HomeProductCardDetailViewSet(generics.RetrieveAPIView):
    queryset = HomeProduct.objects.all()
    serializer_class = HomeProductCardDetailSerializer


class HealthBeautyViewSet(generics.ListAPIView):
    queryset = HealthBeauty.objects.all()
    serializer_class = HealthBeautySerializer

class HealthBeautyCardViewSet(generics.ListAPIView):
    queryset = HealthBeauty.objects.all()
    serializer_class = HealthBeautyCardSerializer


class HealthBeautyCardDetailViewSet(generics.RetrieveAPIView):
    queryset = HealthBeauty.objects.all()
    serializer_class = HealthBeautyCardDetailSerializer


class VitaminsViewSet(generics.ListAPIView):
    queryset = Vitamins.objects.all()
    serializer_class = VitaminsSerializer


class VitaminsCardViewSet(generics.ListAPIView):
    queryset = Vitamins.objects.all()
    serializer_class = VitaminsCardSerializer

class VitaminsCardDetailViewSet(generics.RetrieveAPIView):
    queryset = Vitamins.objects.all()
    serializer_class = VitaminsCardDetailSerializer


class PharmaceuticalViewSet(generics.ListAPIView):
    queryset = Pharmaceutical.objects.all()
    serializer_class = PharmaceuticalSerializer


class PharmaceuticalCardViewSet(generics.ListAPIView):
    queryset = Pharmaceutical.objects.all()
    serializer_class = PharmaceuticalCardSerializer


class PharmaceuticalCardDetailViewSet(generics.RetrieveAPIView):
    queryset = Pharmaceutical.objects.all()
    serializer_class = PharmaceuticalCardDetailSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

