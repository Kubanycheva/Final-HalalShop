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
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name_plural = 'Администратор'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Salesman(UserProfile):
    name_shop = models.CharField(max_length=120, null=True, blank=True)
    categories = models.ManyToManyField('halal_app.Category')
    image = models.ImageField(upload_to='marketer_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.name_shop}'

    class Meta:
        verbose_name_plural = 'Продавец'


class Buyer(UserProfile):
    pass
    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name_plural = 'Покупатель'