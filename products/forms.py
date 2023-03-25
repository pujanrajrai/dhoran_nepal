from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Condition, Categories, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'photo', 'name', 'categories', 'description', 'price', 'stock', 'condition'
        ]

        # widgets = {
        #     "description": CKEditor5Widget(
        #         attrs={"class": "django_ckeditor_5"}, config_name="extends"
        #     )
        # }
