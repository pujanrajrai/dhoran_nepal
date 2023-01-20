from itertools import product
from socket import fromfd
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.http import Http404
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm,ProductForm
from products.models import Categories, MyOrder,Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import F


# listing product categories
class ProductCategoriesListView(ListView):
    model = Categories
    context_object_name = 'categories'
    template_name = 'products/categories/list_categories.html'


# creating product categories
class ProductCategoriesCreatView(SuccessMessageMixin, CreateView):
    form_class = CategoryForm
    template_name = 'products/categories/create_categories.html'
    success_message = 'Product Categories Created Successfully'

    def get_success_url(self):
        return reverse_lazy('product:categories_list')


# updating product categories
class ProductCategoryUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CategoryForm
    model = Categories
    template_name = 'products/categories/update_categories.html'
    success_message = 'Product Category Updated Successfully'

    def get_success_url(self):
        return reverse_lazy('product:categories_list')


# deleting product categories
class ProductCategoryDeleteView(SuccessMessageMixin, DeleteView):
    # specify the model you want to use
    model = Categories
    success_message = 'Product Category Updated Successfully'
    template_name = "products/categories/delete_category.html"

    def get_success_url(self):
        return reverse_lazy('product:categories_list')


# listing product categories
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product/product_list.html'


# creating product
class ProductCreateView(SuccessMessageMixin, CreateView):
    form_class = ProductForm
    template_name = 'products/product/create_product.html'
    success_message = 'Product Categories Created Successfully'

    def get_success_url(self):
        return reverse_lazy('product:product_list')


# updating product categories
class ProductUpdateView(SuccessMessageMixin, UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'products/product/update_product.html'
    success_message = 'Product Updated Successfully'

    def get_success_url(self):
        return reverse_lazy('product:product_list')


# deleting product categories
class ProductDeleteView(SuccessMessageMixin, DeleteView):
    # specify the model you want to use
    model = Product
    success_message = 'Product Deleted Successfully'
    template_name = "products/product/delete_product.html"

    def get_success_url(self):
        return reverse_lazy('product:product_list')


def add_to_cart(request,pk):
    try:
            user=request.user
            product=Product.objects.get(pk=pk)
    
            my_order=MyOrder.objects.filter(my_user=user,product=product,is_paid=False)
            if my_order.exists():
                my_order.update(quantity=F('quantity')+request.GET.get('quantity',1))
            else:
                my_cart=MyOrder(
                    my_user=user,
                    product=product,   
                    quantity=request.GET.get('quantity',1)         
                )
                my_cart.save()
                messages.success(request,
                                f'Added To cart.')
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))