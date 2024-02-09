from django.contrib import admin
from .models import Cart,Cart_item 
# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id',]
    
@admin.register(Cart_item)
class Cart_itemAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','is_active']
    


