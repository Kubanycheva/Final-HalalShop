from django.contrib import admin
from .models import *
from django.utils.html import format_html



class ProductImageInLines(admin.TabularInline):
    model = ProductImage
    extra = 1



class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLines]
    #
    # list_display = ['product_name', 'price', 'display_main_image']
    # def display_main_image(self, obj):
    #     image = obj.images.first()
    #     if image and image.image:
    #         return format_html('<img src="{}" width="60" height="60" style="object-fit: cover;" />', image.image.url)
    #     return '-'
    # display_main_image.short_description = 'Фото'

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)



