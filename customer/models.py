from django.db import models
from unittest.util import _MAX_LENGTH
from admin_panel.models import Products


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=100)
    psw = models.CharField(max_length=10)

    class Meta:
        db_table = "users"

# Create your models here.





class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)

    class Meta:
        db_table = "orders"






















