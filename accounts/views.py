from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.http import Http404
from .forms import RegisterForm,UserForm,ProfileForm
from .models import Profile,User,Order
from cart.models import Cart_item


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

def place_order(request,total=0,quantity=0,grand_total=0):
    cart_items = Cart_item.objects.all().filter(user=request.user,is_active=True)
    for item in cart_items:
        total += (item.product.price)*item.quantity
        quantity += item.quantity
    shipping = 20   
    grand_total = shipping+total  


    context = {
        'cart_items' : cart_items,
        'grand_total' :grand_total,
        'shipping' : shipping,
        'total' : total,
    }
    return render(request,'accounts/place_order.html',context)