from django.shortcuts import redirect, render
from .models import Cart,Cart_item,Coupon
from store.models import Product,Variation
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def add_cart(request,product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        product_variation = []
        if request.method=='POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(variation_category__iexact=key,variation_value__iexact=value)
                    product_variation.append(variation)
                except:
                    pass  
        print(product_variation)          

        item_is_exist = Cart_item.objects.filter(product=product,user=user).exists()
        if item_is_exist:
            cart_item = Cart_item.objects.filter(product=product,user=user)
            ex_var_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            print(product_variation[::-1])    
            print(ex_var_list)    
            if product_variation in ex_var_list[::-1]:
                    # increase the cart item quantity
                    index = ex_var_list.index(product_variation)
                    item_id = id[index]
                    item = Cart_item.objects.get(product=product, id=item_id)
                    item.quantity += 1
                    item.save()    
            else:   
                item = Cart_item.objects.create(product=product, quantity=1, user=user)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
                cart_item = Cart_item.objects.create(
                    product = product,
                    quantity = 1,
                    user = user,
                )
                if len(product_variation) > 0:
                    cart_item.variations.clear()
                    cart_item.variations.add(*product_variation)
                cart_item.save()
        return redirect('cart:cart')
    else:
        return redirect('accounts:login')        
     
def remove_cart_item(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        cart_item = Cart_item.objects.get(product=product,user=request.user)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart')

def remove_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        cart_item = Cart_item.objects.get(product=product,user=request.user)
    cart_item.delete()
    return redirect('cart:cart')

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