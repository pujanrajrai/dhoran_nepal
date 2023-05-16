from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/details/<str:id>', views.product_details, name='product_details'),
    path('search/product/', views.ProductSearch.as_view(), name='search'),
    path('mycart/', views.my_cart, name='cart'),
    path('payment/success/', views.payment, name='payment'),
    path('my_order/', views.my_order, name='my_order'),
    path('order_details/<str:orderid>',
         views.view_order_details, name='view_order_details'),
    path('customer_product/', views.view_customer_product,
         name='view_customer_product'),
]
