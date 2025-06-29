from django.contrib import admin

from .models import Product

# Register your models here.
@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at', 'updated_at')