from django.contrib import admin
from . models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class PrductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
