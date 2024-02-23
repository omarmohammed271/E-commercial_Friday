from django.db import models
from django.urls import reverse
from category.models import Category
from django.utils.text import slugify

# folder = 'product'
def image_product_upload(instance,file_name:str):
    extension = file_name.split('.')[1]
    return f'products\{instance.name}.{extension}'

class Product(models.Model):
    name = models.CharField( max_length=250)
    slug = models.SlugField(unique=True,blank=True,null=True)
    price = models.FloatField(default=0)
    description = models.TextField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to=image_product_upload, height_field=None, width_field=None, max_length=None)
    image2 = models.ImageField(upload_to=image_product_upload, height_field=None, width_field=None, max_length=None,blank=True,null=True)
    image3 = models.ImageField(upload_to=image_product_upload, height_field=None, width_field=None, max_length=None,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def get_url(self): 
        return reverse('store:product_detail',args=[self.category.slug,self.slug])   

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args, **kwargs)


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Product_detail", kwargs={"pk": self.pk})
class Offer(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ratio = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def final_price(self):
        discount = (self.product.price * self.ratio)/100
        new_price = self.product.price - discount
        return new_price
    
    class Meta:
        verbose_name = ("Offer")
        verbose_name_plural = ("Offers")

    def __str__(self):
        return str(self.product)

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_category = 'color',is_active=True)
    def sizes(self):
        return super(VariationManager,self).filter(variation_category = 'size',is_active=True)

choices = (
    ('color','color'),
    ('size','size'),
)
class Variation(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)   
    variation_category = models.CharField( max_length=100,choices=choices) 
    variation_value = models.CharField( max_length=100) 
    is_active = models.BooleanField(default=True)
    created_at =models.DateField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value   