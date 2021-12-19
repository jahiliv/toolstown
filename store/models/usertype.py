from django.db import models

class UserType(models.Model):
    name = models.CharField(max_length=20)