from django.db import models


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


    class Meta:
        verbose_name_plural = 'Мясные продукты'

