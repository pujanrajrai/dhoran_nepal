from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm
from products.models import Categories


class ProductCategoriesListView(ListView):
    model = Categories
    context_object_name = 'categories'
    template_name = 'products/list_categories.html'


class ProductCategoriesCreatView(SuccessMessageMixin,CreateView):
    form_class = CategoryForm
    template_name = 'products/create_categories.html'
    success_message = 'Product Categories Created Successfully'

    def get_success_url(self):
        return reverse_lazy('product:categories_list')


class ProductCategoryUpdateView(SuccessMessageMixin,UpdateView):
    form_class = CategoryForm
    model = Categories
    template_name = 'products/update_categories.html'
    success_message = 'Product Category Updated Successfully'

    def get_success_url(self):
        return reverse_lazy('product:categories_list')


class ProductDeleteView(DeleteView):
    # specify the model you want to use
    model = Categories
    template_name = "products/delete_category.html"

    def get_success_url(self):
        return reverse_lazy('product:categories_list')
