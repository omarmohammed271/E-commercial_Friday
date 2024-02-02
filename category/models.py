from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def image_upload(instance,file_name:str):
    extension = file_name.split('.')[1]
    return f'category/{instance.category_name}.{extension}'
# Create your models here.
class Category(models.Model):
    category_name = models.CharField( max_length=250)
    slug = models.SlugField(unique=True,blank=True,null=True)
    image = models.ImageField( upload_to=image_upload, height_field=None, width_field=None, max_length=None)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def get_url(self):
        return reverse('store:category_slug',args=[self.slug,])
    def __str__(self):
        return self.category_name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})
