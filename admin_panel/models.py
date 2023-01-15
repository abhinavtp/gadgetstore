from django.db import models

# Create your models here.
from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class admin(models.Model):
    username = models.CharField(max_length=10)
    userpass = models.CharField(max_length=10)



class Products(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(max_length=100)
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to="product_images")


    class Meta:
        db_table = 'products'



