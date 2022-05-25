from django.db import models

from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.CharField(max_length=50, null=True)
    # default = 'NULL'

    def __str__(self):
        return f'{self.title} : {self.price} ({self.category})'


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Category)
def product_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


class NewProduct(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.price} (category: {self.category})'



