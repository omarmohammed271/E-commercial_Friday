from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
# Create your views here.
def store(request):
    try:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products,6)  # Show 25 contacts per page.

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    except Product.DoesNotExist:
        pass


    context={
        'products' : page_obj,
    }
    return render(request,'store/store.html',context)