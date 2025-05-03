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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('email', 'password', 'phone_number',
                  'username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')


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


class BirdProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdProduct
        fields = ['id', 'bird_name']


class BirdProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdProduct
        fields = ['id', 'bird_name', 'weight',
                  'price', 'image']


class FishProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishProduct
        fields = ['id', 'fish_name']


class FishProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishProduct
        fields = ['id', 'fish_name', 'weight',
                   'price', 'image']


class FrozenProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrozenProduct
        fields = ['id', 'frozen_name']


class FrozenProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrozenProduct
        fields = ['id', 'frozen_name', 'image', 'price', 'weight']


class DairySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = ['id', 'dairy_name']


class DairyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = ['id', 'dairy_name', 'image', 'price', 'weight']


class BakeryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryProduct
        fields = ['id', 'bakery_name']


class BakeryProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryProduct
        fields = ['id', 'bakery_name', 'image', 'price', 'weight']


class ConfectioneryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfectioneryProduct
        fields = ['id', 'product_name']


class ConfectioneryProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfectioneryProduct
        fields = ['id', 'product_name', 'image', 'price', 'weight']


class ReadyMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyMeal
        fields = ['id', 'meal_name']


class ReadyMealCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyMeal
        fields = ['id', 'meal_name', 'image', 'price', 'weight']


class GrocerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrocerProduct
        fields = ['id', 'grocer_name']


class GrocerProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrocerProduct
        fields = ['id', 'grocer_name', 'image', 'price', 'weight']


class DrinkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkProduct
        fields = ['id', 'drink_name']


class DrinkProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkProduct
        fields = ['id', 'drink_name', 'image', 'price', 'weight']


class BabyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyProduct
        fields = ['id', 'product_name']


class BabyProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyProduct
        fields = ['id', 'product_name', 'weight', 'price', 'image']


class HomeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProduct
        fields = ['id', 'home_name']


class HomeProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProduct
        fields = ['id', 'home_name', 'weight', 'price', 'image']


class HealthBeautySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthBeauty
        fields = ['id', 'product_name']


class HealthBeautyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthBeauty
        fields = ['id', 'product_name', 'weight', 'price', 'image']


class VitaminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamins
        fields = ['id', 'product_name']


class VitaminsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamins
        fields = ['id', 'product_name', 'weight', 'price', 'image']


class PharmaceuticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmaceutical
        fields = ['id', 'product_name']


class PharmaceuticalCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmaceutical
        fields = ['id', 'product_name', 'weight', 'price', 'image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    baby_category = BabyProductSerializer(many=True, read_only=True)
    category_meats = MeatsProductSerializer(many=True, read_only=True)
    bird_eggs = BirdProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'baby_category', 'category_meats', 'bird_eggs']



