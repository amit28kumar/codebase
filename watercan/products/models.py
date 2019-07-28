# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import (CharField, DateTimeField, IntegerField, Model, URLField, ForeignKey, BooleanField, ImageField)


class Product(Model):
    name = CharField(max_length=200,blank=False, null=False)

    class Meta:
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
        unique_together = (('name'),)

class ProductDetails(Model):
    product = ForeignKey(Product, related_name='product_details')
    category = CharField(max_length=200, blank=False, null=False)
    price = IntegerField(default=0, null=True)
    image = ImageField(upload_to=None, height_field=None, width_field=None, blank=True)
    description = CharField(max_length=250, blank=True, null=True)
    rating = IntegerField(default=5, null=True)
    availability = BooleanField(default=True)

    class Meta:
        verbose_name = ('Product Detail')
        verbose_name_plural = ('Product Details')
        unique_together = (('product', 'category'),)
