from django.contrib import admin
from .models import Product


class ProductAdminView(admin.ModelAdmin):
    list_display = ["title", "content", "price"]


admin.site.register(Product, ProductAdminView)
