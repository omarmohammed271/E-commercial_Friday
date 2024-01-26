from django.db import models
from category.models import Category

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Product_detail", kwargs={"pk": self.pk})
