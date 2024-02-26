from django.contrib import admin
from .models import Cart,Cart_item,Coupon 
# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id',]
    
@admin.register(Cart_item)
class Cart_itemAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','variations','is_active']
    
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['name','value','created_at','is_active']


