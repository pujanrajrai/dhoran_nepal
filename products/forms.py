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
            'user', 'photo', 'name', 'categories', 'description', 'price', 'stock', 'condition'
        ]

    def __init__(self, user=None, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user
        self.fields['user'].widget = forms.HiddenInput()

        # widgets = {
        #     "description": CKEditor5Widget(
        #         attrs={"class": "django_ckeditor_5"}, config_name="extends"
        #     )
        # }
