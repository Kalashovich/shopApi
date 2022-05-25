"""shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from order.views import CreateOrderView, UserOrderList, UpdateOrderStatusView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/basket/', include('basket.urls')), #cart
    path('api/v1/orders/', CreateOrderView.as_view()),
    path('api/v1/orders/own/', UserOrderList.as_view()),
    path('api/v1/orders/<int:pk>/', UpdateOrderStatusView.as_view()),




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
