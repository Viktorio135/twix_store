from django.contrib import admin

from goods.models import Categories, Product
from user.models import User


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = { 'slug': ('name',) }


@admin.register(Product) 
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = { 'slug': ('name',) }

