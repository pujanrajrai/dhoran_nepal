from django.contrib import admin
from products.models import Categories, Condition, Product

# Register your models here.

admin.site.register(Categories)
admin.site.register(Condition)
admin.site.register(Product)
