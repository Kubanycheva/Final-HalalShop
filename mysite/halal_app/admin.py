from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserProfile)
admin.site.register(Salesman)
admin.site.register(Buyer)
admin.site.register(Category)
admin.site.register(MeatsProduct)
admin.site.register(BirdProduct)
admin.site.register(FishProduct)
admin.site.register(FrozenProduct)
admin.site.register(Dairy)
admin.site.register(BakeryProduct)
admin.site.register(ConfectioneryProduct)
admin.site.register(ReadyMeal)
admin.site.register(GrocerProduct)
admin.site.register(DrinkProduct)
admin.site.register(BabyProduct)
admin.site.register(HomeProduct)
admin.site.register(HealthBeauty)
admin.site.register(Vitamins)
admin.site.register(Pharmaceutical)
