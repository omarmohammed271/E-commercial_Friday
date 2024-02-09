from django.shortcuts import redirect, render
from .models import Cart,Cart_item
from store.models import Product
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(_cart_id(request)) 
    except:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )     
        cart.save() 
    try:
        cart_item = Cart_item.objects.get(product=product,cart=cart)
        cart_item.quantity +=1
        cart_item.save()
    except:
        cart_item = Cart_item.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )     
        cart_item.save()   
        return redirect('cart:cart')

def cart(request):
    cart_items = Cart_item.objects.all().filter(is_active=True)

    context = {
        'cart_items':cart_items,
    }
    return render(request,'cart/cart.html',context)