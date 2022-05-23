from rest_framework import serializers
from product.models import Product
from basket.models import Order


class OrderSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    count = serializers.IntegerField()

    def validate(self, attrs):
        data = {}
        try:
            product = Product.objects.get(
                pk=attrs['product']
            )
        except Product.DoesNotExist:
            raise serializers.ValidationError('Product not found')
        count = attrs['count']
        data['product'] = product.pk
        data['count'] = count
        return data

    def save(self, **kwargs):
        data = self.validated_data
        user = kwargs['user']
        product = Product.objects.get(pk=data['product'])
        Order.objects.create(
            product=product,
            user=user,
            count=data['count'],
        )