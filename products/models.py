import os
from django.db import models
from django.db.models.signals import pre_save, post_save

from django.urls import reverse
from.utils import unique_slug_generator

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    list =[]
    for i in range(len(name)):
        if name[i] != ' ':
            list.append(name[i])
    ''.join(list)
    final_filename = f'{list}{ext}'
    return final_filename

class Product(models.Model):
    title           = models.CharField(max_length =20)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, default=100, max_digits=10)
    #image          = models.FileField(upload_to=upload_image_path, null=True, blank=True)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    slug            = models.SlugField(blank= True, unique=True)

    def get_absolute_url(self):
        #return f'{self.slug}'
        return reverse("details", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)