from rest_framework import serializers
from models import Product, ProductDetails


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name',)


class ProductDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetails
        fields = ('id', 'product', 'category', 'price', 'image', 'description', 'rating', 'availability')
