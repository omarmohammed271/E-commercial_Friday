from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Cart,Cart_item,Coupon,Variation
from store.models import Product
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
@login_required(login_url='accounts:login')
def add_cart(request,product_id):
    
    user = request.user
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        color = request.POST['color']
        size = request.POST['size']
        variation = Variation()
        variation.product = product
        variation.color_value = color
        variation.size_value = size
        variation.save()
        cart_item = Cart_item()
        cart_item.user = request.user
        cart_item.product = product
        cart_item.quantity=1
        cart_item.variations = variation
        cart_item.save()
    
    variation = Variation.objects.filter(product=product)
        
    try:
        cart_item = Cart_item.objects.get(product=product,user=user) 
        cart_item.save()
    except Cart_item.DoesNotExist:
        cart_item = Cart_item.objects.create(
            product=product,
            user = user,
            quantity=1
        )
        cart_item.variations=variation  
        cart_item.save()

    
    return redirect('cart:cart') 
def remove_cart_item(request,product_id):
    
    product = Product.objects.get(id=product_id)
    cart_item = Cart_item.objects.get(product=product,user=request.user)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart')

def remove_cart(request,product_id):

    product = Product.objects.get(id=product_id)
    cart_item = Cart_item.objects.get(product=product,user=request.user)
    cart_item.delete()
    return redirect('cart:cart')

@login_required(login_url='accounts:login')
def cart(request,total=0,quantity=0,grand_total=0,coupon=None,discount=0):
    try:
        cart_items = Cart_item.objects.all().filter(user=request.user,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price)*cart_item.quantity
            quantity += cart_item.quantity
        if request.method == "POST":
            discount = request.POST['coupon']
            if discount:
                try:
                    coupon = Coupon.objects.get(value=discount)
                    shipping = 20   
                    grand_total = shipping+total 
                    discount = (grand_total*coupon.ratio)/100
                    grand_total = grand_total-discount
                except:
                    pass 
        else:            
            shipping = 20   
            grand_total = shipping+total 
        
    except Cart_item.DoesNotExist:
        pass
    print(total)
    context = {
        'cart_items':cart_items,
        'total':total,
        'quantity':quantity,
        'grand_total':grand_total,
        'shipping': shipping,
        'discount':discount,
    }
    return render(request,'cart/cart.html',context)




# try:
        
#         cart_item = Cart_item.objects.get(product=product,user=user) 
#         cart_item.quantity += 1
#         cart_item.save()
#     except Cart_item.DoesNotExist:
#         cart_item = Cart_item.objects.create(
#             product=product,
#             user = user,
#             quantity=1
#         )
#         cart_item.variations.color_value=color   
#         cart_item.variations.size_value=size   
#         cart_item.save()