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
    variations = models.ForeignKey(Variation,on_delete=models.CASCADE, blank=True)
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


    

 
