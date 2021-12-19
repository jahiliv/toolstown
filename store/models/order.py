from django.db import models
from .product import Product
from .status import Status
from django.contrib.auth.models import User
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    baseprice = models.FloatField(default=0.00)
    borrowprice = models.FloatField(default=0.00)
    deliveryfee = models.FloatField(default=0.00)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    deliverydate = models.DateField()
    ordereddate = models.DateField(default=datetime.datetime.today)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    is_active = models.IntegerField(default=1)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='1')

    # def __str__(self):
    #     return self.user

    def save(self, *args, **kwargs):
        if self.deliverydate is None:
            self.deliverydate = self.ordereddate.date() + datetime.timedelta(days=7)
        super(Order, self).save(*args, **kwargs)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer_pending(customer_id):
        return Order.objects.filter(user = customer_id, status = 1).order_by('-created_at')
    
    @staticmethod
    def get_orders_by_customer_delivered(customer_id):
        return Order.objects.filter(user = customer_id, status = 2).order_by('-created_at')

    @staticmethod
    def get_orders_by_customer_compeleted(customer_id):
        return Order.objects.filter(user = customer_id, status = 3).order_by('-created_at')

    


