from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/details/<str:id>', views.product_details, name='product_details'),
    path('search/product/',views.ProductSearch.as_view(),name='search'),
    path('mycart/',views.my_cart,name='cart'),
    path('esewa/success/',views.esewa_success,name='esewa_success'),
]
