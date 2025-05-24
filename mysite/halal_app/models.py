from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'),
        reset_password_token.key
    )

    send_mail(
        # Subject
        "Password Reset for {title}".format(title="Some website title"),
        # Message
        email_plaintext_message,
        # From email
        "noreply@somehost.local",
        # Recipient list
        [reset_password_token.user.email]
    )


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Администратор'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Salesman(UserProfile):
    created_date = models.DateTimeField(auto_now=True)
    created_moth = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='marketer_images/', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Продавец'


class Buyer(UserProfile):
    image = models.ImageField(upload_to='buyer_images/', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Покупатель'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Категория'


class MeatsProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_meats')
    meets_name = models.CharField(max_length=32, verbose_name='название')
    price = models.PositiveIntegerField(default=0)
    expiration_period = models.IntegerField(default=24, verbose_name='срок годности')
    created_at = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Вес продукта (в кг)')
    expiration_period = models.IntegerField(default=10, verbose_name='срок годности в днях')
    composition = models.TextField(verbose_name='состав')
    storage_condition = models.TextField(verbose_name='условия хранение')
    packaging = models.TextField(verbose_name='упаковка')
    equipment = models.TextField(null=True, blank=True, verbose_name='коплектация')
    image = models.ImageField(upload_to='meats_images/', null=True, blank=True)

    def get_expiration_date(self):
        return self.created_at + timedelta(days=self.expiration_period * 30)

    def __str__(self):
        return self.meets_name

    class Meta:
        verbose_name_plural = 'Мясные продукты'


class BirdProduct(models.Model):
    bird_name = models.CharField(max_length=32, verbose_name='название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='мясо птицы и яйца', related_name='bird_eggs')
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    expiration_period = models.IntegerField(default=10, verbose_name='Срок годности')
    composition = models.TextField(blank=True, null=True, verbose_name='состав')
    storage_conditions = models.TextField(verbose_name='Условия хранения, от 0 до +4°C')
    packaging = models.TextField(verbose_name='Упаковка')
    equipment = models.TextField(blank=True, null=True, verbose_name='комлектация')
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='bird_images/', null=True, blank=True)
    created_date = models.DateField(auto_now=True)



    def get_expiration_date(self):
        return self.created_at + timedelta(days=self.expiration_period)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bird_name

    class Meta:
        verbose_name_plural = 'Мясо птицы и яйца'


class FishProduct(models.Model):
    fish_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fish_products')
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    expiration_period = models.IntegerField(default=10, verbose_name='Срок годности')
    composition = models.TextField(blank=True, null=True, verbose_name='состав')
    storage_conditions = models.TextField(verbose_name='Условия хранения, от 0 до +4°C')
    packaging = models.TextField(verbose_name='Упаковка')
    equipment = models.TextField(blank=True, null=True, verbose_name='комлектация')
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='fish_images/', null=True, blank=True)


    def get_expiration_date(self):
        return self.created_at + timedelta(days=self.expiration_period)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fish_name

    class Meta:
        verbose_name_plural = 'Рыба и морепродукты'


class FrozenProduct(models.Model):
    frozen_name = models.CharField(max_length=32, verbose_name='замороженные продукты')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='frozen_category')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    frozen_date = models.DateField()
    image = models.ImageField(upload_to='frozen_images/', null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='вес', null=True, blank=True)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.frozen_name

    class Meta:
        verbose_name_plural = 'Замороженные продукты'


class Dairy(models.Model):
    dairy_name = models.CharField(max_length=32, verbose_name='молочные продукты')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dairy_category')
    image = models.ImageField(upload_to='dairy_image')
    price = models.PositiveIntegerField()
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='вес', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='срока годности')
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.dairy_name

    class Meta:
        verbose_name_plural = ' Молочные продукты'


class BakeryProduct(models.Model):
    bakery_name = models.CharField(max_length=32, verbose_name='выпечка название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='bakery_category')
    image = models.ImageField(upload_to='image_bakery')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='вес', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='срока годности')
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.bakery_name

    class Meta:
        verbose_name_plural = 'Мука, хлеб и выпечка'


class ConfectioneryProduct(models.Model):
    product_name = models.CharField(max_length=32, verbose_name='Кондитерское название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_cake')
    image = models.ImageField(upload_to='image_cake')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='вес', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='срока годности')
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Кондитерские изделия'


class ReadyMeal(models.Model):
    meal_name = models.CharField(max_length=32, verbose_name='название продукты')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ready_category')
    image = models.ImageField(upload_to='image_ready')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='вес', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='срока годности')
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.meal_name

    class Meta:
        verbose_name_plural = 'Готовая еда'


class GrocerProduct(models.Model):
    grocer_name = models.CharField(max_length=32, verbose_name='название продукты')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='grocery_category')
    image = models.ImageField(upload_to='image_grocery')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='вес', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='срока годности')
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.grocer_name

    class Meta:
        verbose_name_plural = 'Бакалея'


class DrinkProduct(models.Model):
    drink_name = models.CharField(max_length=100, verbose_name='Название напитка')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    volume = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Объем напитка')
    image = models.ImageField(upload_to='drink_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='drink_category')
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.drink_name

    class Meta:
        verbose_name_plural = 'Напитки'


class BabyProduct(models.Model):
    product_name = models.CharField(max_length=32, verbose_name='название товары')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='bady_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='baby_category')
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Товары для детей'


class HomeProduct(models.Model):
    home_name = models.CharField(max_length=32, null=True, blank=True, verbose_name='товары для дома')
    image = models.ImageField(upload_to='home_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='home_category')
    created_date = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.home_name

    class Meta:
        verbose_name_plural = 'Товары для дома'


class HealthBeauty(models.Model):
    product_name = models.CharField(max_length=32, null=True, blank=True, verbose_name='название товара')
    image = models.ImageField(upload_to='beauty_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='beauty_category')
    created_date = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Здоровье и красота'


class Vitamins(models.Model):
    product_name = models.CharField(max_length=32, null=True, blank=True, verbose_name='название витамины')
    image = models.ImageField(upload_to='vitamins_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vitamins_category')
    created_date = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Бад и витамины'


class Pharmaceutical(models.Model):
    product_name = models.CharField(max_length=32, null=True, blank=True, verbose_name='название лекарств')
    image = models.ImageField(upload_to='medicine_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='medicine_category')
    created_date = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Фармацевтика'
















