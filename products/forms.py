from django import forms
from .models import Condition, Categories, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
