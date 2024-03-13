from django.contrib import admin
from .models import Cart,Cart_item,Coupon,Order,OrderProduct
# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id',]
    
@admin.register(Cart_item)
class Cart_itemAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','is_active']
    
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['name','value','created_at','is_active']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'user','f_name','l_name','city','order_total','is_active','created_at','updated_at'


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = 'user','order','product','variations','ordered','created_at','updated_at'


