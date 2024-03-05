from django.contrib import admin
from .models import Profile,Orderr,OrderProduct
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone']

@admin.register(Orderr)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','f_name','l_name','email','phone','order_total']

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass
    
