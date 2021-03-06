from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=150)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    price = models.FloatField(_("Price"))
    image = models.ImageField(_("Image"), upload_to="products", null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.SET_NULL, null=True, blank=True) # Or Cascade

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'[{self.title}:{self.price}]'