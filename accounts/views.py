from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.http import Http404
from .forms import RegisterForm,UserForm,ProfileForm
from .models import Profile,User,Orderr,OrderProduct
from cart.models import Cart_item
from store.models import Product


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)

            return redirect('accounts:profile')
        
      
    else:
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form,})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('accounts:profile')
        else:
            raise Http404("Page not found")


    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')
    

def profile(request):
    
    return render(request,'accounts/profile.html')

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        u = UserForm(request.POST,request.FILES,instance=request.user)
        p = ProfileForm(request.POST,request.FILES,instance=profile)
        if u.is_valid() and p.is_valid():
            u.save()
            p.save()
            return redirect('accounts:profile')
    else:

        u = UserForm(instance=request.user)
        p = ProfileForm(instance=profile)

    context = {
        'userForm':u,
        'profileForm' :p,
    }
    return render(request,'accounts/edit_profile.html',context)

def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if password == confirm_password :
            print('Step1')
            user_exist = User.objects.filter(email=email).exists()
            print('Step2')
            if user_exist:
                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()
                return redirect('accounts:login')




    return render(request,'accounts/reset_password.html')

def place_order(request,total=0,quantity=0,grand_total=0,address2=None):
    cart_items = Cart_item.objects.all().filter(user=request.user,is_active=True)
    for item in cart_items:
        total += (item.product.price)*item.quantity
        quantity += item.quantity
    shipping = 20   
    grand_total = shipping+total  
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        order = Orderr.objects.create(
            user=request.user,
            f_name=f_name,l_name=l_name,
            email=email,
            phone=phone,
            address1=address1,address2=address2,
            city=city,
            order_total= grand_total,
            is_ordered=True,
        )
        order.save()
        for item in cart_items:
            orderproduct = OrderProduct()
            orderproduct.order_id = order.id
            orderproduct.user_id = request.user.id
            orderproduct.product = item.product
            orderproduct.variations = item.variations
            orderproduct.quantity = item.quantity
            orderproduct.product_price=item.product.price
            orderproduct.ordered = True
            orderproduct.save()
            product = Product.objects.get(id=item.product_id)
            product.stock -= item.quantity
            product.save()    
        Cart_item.objects.filter(user=request.user).delete()
        return redirect('home')    

    context = {
        'cart_items' : cart_items,
        'grand_total' :grand_total,
        'shipping' : shipping,
        'total' : total,
    }
    return render(request,'accounts/place_order.html',context)