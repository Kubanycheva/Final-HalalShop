from datetime import datetime

from django.urls import reverse
from django_rest_passwordreset.models import ResetPasswordToken
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'),
        reset_password_token.key
    )

    send_mail(
        "Password Reset for {title}".format(title="Some website title"),
        email_plaintext_message,
        "noreply@somehost.local",
        [reset_password_token.user.email]
    )


class VerifyResetCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Email пользователя
    reset_code = serializers.IntegerField()  # 4-значный код
    new_password = serializers.CharField(write_only=True)  # Новый пароль

    def validate(self, data):
        email = data.get('email')
        reset_code = data.get('reset_code')

        # Проверяем, существует ли указанный код для email
        try:
            token = ResetPasswordToken.objects.get(user__email=email, key=reset_code)
        except ResetPasswordToken.DoesNotExist:
            raise serializers.ValidationError("Неверный код сброса или email.")

        data['user'] = token.user
        return data

    def save(self):
        user = self.validated_data['user']
        new_password = self.validated_data['new_password']

        # Устанавливаем новый пароль
        user.set_password(new_password)
        user.save()


class UserSerializer(serializers.ModelSerializer): # Регистрация для обычных пользователей
    class Meta:
        model = UserProfile
        fields = ('email', 'password', 'phone_number',
                  'username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # validated_data['role'] = 'User' (with role)
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        access_token_expiration = datetime.fromtimestamp(refresh.access_token['exp']).isoformat()
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'access_token_expiration': access_token_expiration,
        }


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        access_token_expiration = datetime.fromtimestamp(refresh.access_token['exp']).isoformat()
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'access_token_expiration': access_token_expiration,
        }


class UserLogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs.get('refresh_token')
        if not refresh_token:
            raise serializers.ValidationError('Refresh токен не предоставлен.')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError as e:
            raise serializers.ValidationError('Недействительный токен.')

        return attrs

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'phone_number']


class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = ['id', 'username', 'phone_number']


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'username', 'phone_number']


class MeatsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeatsProduct
        fields = ['id', 'meets_name']


class MeatsProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeatsProduct
        fields = ['id', 'meets_name', 'price', 'weight' ]


class MeatsProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeatsProduct
        fields = ['id', 'meets_name', 'price', 'weight', 'expiration_period']


class BirdProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdProduct
        fields = ['id', 'bird_name']


class BirdProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdProduct
        fields = ['id', 'bird_name',
                  'price', 'image']


class BirdProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdProduct
        fields = ['id', 'bird_name',
                  'price', 'image', 'expiration_period']

class FishProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishProduct
        fields = ['id', 'fish_name']


class FishProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishProduct
        fields = ['id', 'fish_name',
                   'price', 'image']


class FishProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishProduct
        fields = ['id', 'fish_name', 'weight',
                   'price', 'image', 'expiration_period']

class FrozenProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrozenProduct
        fields = ['id', 'frozen_name']


class FrozenProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrozenProduct
        fields = ['id', 'frozen_name', 'image', 'price', 'weight']


class FrozenProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrozenProduct
        fields = ['id', 'frozen_name', 'image', 'price', 'weight', 'description']


class DairySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = ['id', 'dairy_name']


class DairyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = ['id', 'dairy_name', 'image', 'price', 'weight']


class DairyCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = ['id', 'dairy_name', 'image', 'price', 'weight', 'description']


class BakeryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryProduct
        fields = ['id', 'bakery_name']


class BakeryProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryProduct
        fields = ['id', 'bakery_name', 'image', 'price', 'weight']

class BakeryProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryProduct
        fields = ['id', 'bakery_name', 'image', 'price', 'weight', 'description']


class ConfectioneryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfectioneryProduct
        fields = ['id', 'product_name']


class ConfectioneryProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfectioneryProduct
        fields = ['id', 'product_name', 'image', 'price', 'weight']


class ConfectioneryProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfectioneryProduct
        fields = ['id', 'product_name', 'image', 'price', 'weight', 'description']


class ReadyMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyMeal
        fields = ['id', 'meal_name']


class ReadyMealCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyMeal
        fields = ['id', 'meal_name', 'image', 'price', 'weight']


class ReadyMealCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyMeal
        fields = ['id', 'meal_name', 'image', 'price', 'weight', 'description']


class GrocerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrocerProduct
        fields = ['id', 'grocer_name']


class GrocerProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrocerProduct
        fields = ['id', 'grocer_name', 'image', 'price', 'weight']

class GrocerProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrocerProduct
        fields = ['id', 'grocer_name', 'image', 'price', 'weight', 'description']

class DrinkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkProduct
        fields = ['id', 'drink_name']


class DrinkProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkProduct
        fields = ['id', 'drink_name', 'image', 'price']


class DrinkProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkProduct
        fields = ['id', 'drink_name', 'image', 'price', 'description']


class BabyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyProduct
        fields = ['id', 'product_name']


class BabyProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyProduct
        fields = ['id', 'product_name', 'price', 'image']


class BabyProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyProduct
        fields = ['id', 'product_name', 'price', 'image', 'description']

class HomeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProduct
        fields = ['id', 'home_name']


class HomeProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProduct
        fields = ['id', 'home_name', 'price', 'image']


class HomeProductCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProduct
        fields = ['id', 'home_name', 'price', 'image', 'description']


class HealthBeautySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthBeauty
        fields = ['id', 'product_name']


class HealthBeautyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthBeauty
        fields = ['id', 'product_name', 'price', 'image']


class HealthBeautyCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthBeauty
        fields = ['id', 'product_name', 'price', 'image', 'description']



class VitaminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamins
        fields = ['id', 'product_name']


class VitaminsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamins
        fields = ['id', 'product_name', 'price', 'image']

class VitaminsCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamins
        fields = ['id', 'product_name', 'price', 'image', 'description']


class PharmaceuticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmaceutical
        fields = ['id', 'product_name']


class PharmaceuticalCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmaceutical
        fields = ['id', 'product_name', 'price', 'image']


class PharmaceuticalCardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmaceutical
        fields = ['id', 'product_name', 'price', 'image', 'description']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']




