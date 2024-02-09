from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Product,Offer
from category.models import Category
# Create your views here.
def store(request,category_slug=None):
    
    if category_slug != None:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category,is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)

    paginator = Paginator(products,6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        'products' : page_obj,
        
    }
    return render(request,'store/store.html',context)

def product_detail(request,category_slug,product_slug,offer=None):
    category = Category.objects.get(slug=category_slug)
    product = get_object_or_404(Product,slug=product_slug,category=category)
    try:
        offer = Offer.objects.get(product=product)
    except:
        pass    
    context = {
        'product':product,
        'offer' : offer,
    }
    return render(request,'store/product_detail.html',context)

def offer(request):
    
    return render(request,'store/offers.html')