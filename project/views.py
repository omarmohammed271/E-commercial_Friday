from django.shortcuts import render
from django.db.models import Count
from category.models import Category
from django.http import HttpResponse
# Create your views here.
def home(request):
    try:
        categories = Category.objects.all().annotate(product_count=Count('product'))
    except Category.DoesNotExist:
        return HttpResponse('Error 404')
    context = {
        'categories':categories,
    }
    return render(request,'home/home.html',context)