from django.db import models
from django.contrib.auth.models import User
from store.models import Product,Variation

# Create your models here.
class Cart(models.Model):

    cart_id = models.CharField(max_length=250)
    date_field = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Cart")
        verbose_name_plural = ("Carts")

    def __str__(self):
        return self.cart_id

class Cart_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    vartions = models.ForeignKey(Variation, on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)


    def sub_total(self):
        return (self.product.price)* self.quantity
    class Meta:
        verbose_name = ("Cart_item")
        verbose_name_plural = ("Cart_items")

    def __str__(self):
        return str(self.product)

class Coupon(models.Model):
    name = models.CharField(max_length=150)
    value = models.CharField(max_length=100)
    ratio = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = ("Coupon")
        verbose_name_plural = ("Coupons")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Coupon_detail", kwargs={"pk": self.pk})


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    f_name = models.CharField( max_length=250)
    l_name = models.CharField( max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address1 = models.CharField( max_length=250)
    address2 = models.CharField( max_length=250,blank=True,null=True)
    city = models.CharField( max_length=150)
    order_total = models.FloatField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.f_name} {self.l_name}'

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("OrderProduct")
        verbose_name_plural = ("OrderProducts")

    def __str__(self):
        return f"{self.order} {self.user}"


 
