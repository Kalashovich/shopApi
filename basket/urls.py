from django.urls import path, include
from basket import views
from django.contrib import admin



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('order/', views.BasketApiView.as_view()),
    # path('api/v1/account/', include('account.urls')),
    # path('api/v1/basket/', include('basket.urls')),
]


