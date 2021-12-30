from django.contrib import admin
from myapp.models import Category, Product

    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["id", "category_name", "created_at", "updated_at"]
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["id", "product_name", "category", "created_at", "updated_at"]
    