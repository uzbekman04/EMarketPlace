from django.contrib import admin
from .models import Product,Category
# Register your models here
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','price']
    ordering = ('created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

