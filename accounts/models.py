from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cart.models import Cart_item
from store.models import Product,Variation
# Create your models here.
# Person = user + profile

def profile_upload(instance,filename:str):
    extension = filename.split('.')[1]
    return f'accounts/{instance.user}.{extension}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to=profile_upload,blank=True)
    phone = models.CharField(max_length=15)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return str(self.user)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)    


class Orderr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=150)
    l_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    order_total = models.FloatField()
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Orderr, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ForeignKey(Variation, on_delete=models.CASCADE, blank=True)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name    





