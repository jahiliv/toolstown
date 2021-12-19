from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.usertype import UserType
from .models.extendeduser import ExtendedUser
from .models.order import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category']

class ProductCategory(admin.ModelAdmin):
    list_display = ['name']

class UserCategory(admin.ModelAdmin):
    list_display = ['name']

class ExtendedUsers(admin.ModelAdmin):
    list_display = ['nid']

class OrderPlacement(admin.ModelAdmin):
    list_display = ['user','address','phone','created_at','status']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, ProductCategory)
admin.site.register(ExtendedUser, ExtendedUsers)
admin.site.register(UserType, UserCategory)
admin.site.register(Order, OrderPlacement)