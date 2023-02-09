from django.contrib import admin
from django.urls import path

from products.views import create_product, list_products

urlpatterns = [

    path('create-product/', create_product),
    path('list-products/', list_products),

]