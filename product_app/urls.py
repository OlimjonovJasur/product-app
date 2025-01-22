from django.urls import path

from .views import categories_view, products_for_categories, product_detail_view

urlpatterns = [
    path('', categories_view, name='categories'),
    path('category/<int:category_id>/products/', products_for_categories, name='products_for_category'),
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),
]