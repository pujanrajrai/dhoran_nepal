from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


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
    photo = models.ImageField(upload_to='products/image/', verbose_name='Product Image')
    name = models.CharField(max_length=100, verbose_name='Product Name')
    categories = models.ManyToManyField(Categories, verbose_name='Categories')
    price = models.PositiveIntegerField(verbose_name='Price')
    description = CKEditor5Field('Text', config_name='extends')
    stock = models.PositiveIntegerField(verbose_name='Total Stock')
    Condition = models.ForeignKey(Condition, on_delete=models.CASCADE, verbose_name='Product Current Condition')
    create_date = models.DateField(auto_now=True)
    total_click = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
