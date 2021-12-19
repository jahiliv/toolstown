from django.db import models
from .usertype import UserType
from django.contrib.auth.models import User


class ExtendedUser(models.Model):
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE,default=4)
    nid = models.CharField(max_length=20)
    age = models.IntegerField()
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    