from django.db import models
from .category import Category
# from django.db.models.base import Model



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=100)
    base_price = models.FloatField(default=0.00)
    borrow_price = models.FloatField(default=0.00)
    description = models.CharField(max_length=200, default='')
    quantity = models.IntegerField(default=0)
    last_added_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    is_active = models.IntegerField(default=1)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    
    @staticmethod
    def get_products_by_categoryID(categoryID):
        if(categoryID):
            return Product.objects.filter(category= categoryID)
        else:
            return Product.objects.all()

    
    @staticmethod
    def get_products_by_id(product_id):
        return Product.objects.filter(id__in = product_id)


     

