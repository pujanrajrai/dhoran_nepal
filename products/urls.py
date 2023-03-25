from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # product category
    path('list/category/', views.ProductCategoriesListView.as_view(), name='categories_list'),
    path('create/category/', views.ProductCategoriesCreatView.as_view(), name='categories_create'),
    path('update/category/<str:pk>', views.ProductCategoryUpdateView.as_view(), name='update_category'),
    path('delete/category/<str:pk>', views.ProductCategoryDeleteView.as_view(), name='delete_category'),

    # product
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('update/product/<str:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('delete/product/<str:pk>', views.ProductDeleteView.as_view(), name='delete_product'),

    path('addto/cart/<str:pk>/',views.add_to_cart,name="add_to_cart"),
    path('order/',views.my_order,name="order_list"),
    path('order_details/<str:orderid>', views.view_order_details, name='view_order_details'),
    path('send_item/<str:orderid>', views.send_item, name='send_item'),
    path('delivered/<str:orderid>', views.item_delivered, name='item_delivered'),


]

