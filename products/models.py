from itertools import product
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from accounts.models import CustomUser


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, null=True, blank=True)
    photo = models.ImageField(
        upload_to='products/image/', verbose_name='Product Image')
    name = models.CharField(max_length=100, verbose_name='Product Name')
    categories = models.ManyToManyField(Categories, verbose_name='Categories')
    tags = models.CharField(max_length=500, blank=True,
                            null=True, verbose_name='Product Tags')
    price = models.PositiveIntegerField(verbose_name='Price')
    description = CKEditor5Field('Description', config_name='extends')
    stock = models.PositiveIntegerField(verbose_name='Total Stock')
    condition = models.ForeignKey(
        Condition, on_delete=models.CASCADE, verbose_name='Product Current Condition')
    total_sales = models.PositiveBigIntegerField(default=0)
    create_date = models.DateField(auto_now=True)
    total_click = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MyOrder(models.Model):
    my_user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, verbose_name='my_user', null=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, verbose_name='my_product', null=True)
    quantity = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)
    txid = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    is_order_placed = models.BooleanField(default=False)
    is_order_sent = models.BooleanField(default=False)
    is_order_delivered = models.BooleanField(default=False)

