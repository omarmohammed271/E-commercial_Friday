from django.db import models
from store.models import Product
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
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = ("Cart_item")
        verbose_name_plural = ("Cart_items")

    def __str__(self):
        return str(self.product)


    

 
