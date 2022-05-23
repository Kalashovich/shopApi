from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from product.models import NewProduct, Category
from product import serializers
from rest_framework import permissions


class ProductViewSet(ModelViewSet):
    queryset = NewProduct.objects.all()
    serializer_class = serializers.ProductSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get_permissions(self):
        # if self.action == 'list':
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny(), ]
        else:
            return [permissions.IsAuthenticated(), ]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser, ]
