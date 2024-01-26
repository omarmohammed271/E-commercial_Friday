from django.contrib import admin
from .models import Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','slug']
    









# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['category_name','slug']


# admin.site.register(Category,CategoryAdmin)
