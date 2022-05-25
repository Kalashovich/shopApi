from rest_framework import serializers
from product.models import Product, NewProduct, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProduct
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProduct
        fields = ('id', 'name', 'price', 'image',)


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Category
        # fields = ('name',)
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = ProductListSerializer(instance.products.all(), many=True).data
        return representation




