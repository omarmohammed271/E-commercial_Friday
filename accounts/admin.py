from django.contrib import admin
from .models import Profile,Order
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','f_name','l_name','email','phone']
