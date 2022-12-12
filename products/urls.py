from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # product category
    path('list/category/', views.ProductCategoriesListView.as_view(), name='categories_list'),
    path('create/category/', views.ProductCategoriesCreatView.as_view(), name='categories_create'),
    path('update/category/<str:pk>', views.ProductCategoryUpdateView.as_view(), name='update_category'),
    path('delete/category/<str:pk>', views.ProductDeleteView.as_view(), name='delete_category'),

]
