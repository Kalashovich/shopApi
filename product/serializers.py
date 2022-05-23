from rest_framework import serializers
from product.models import Product, NewProduct, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProduct
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ('name',)
        fields = '__all__'



