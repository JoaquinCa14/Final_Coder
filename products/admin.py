from django.contrib import admin

from products.models import Products

# admin.site.register(Products)

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price' , 'stock')
    list_filter = ('stock' , 'price')
    search_fields = ('name',)
    