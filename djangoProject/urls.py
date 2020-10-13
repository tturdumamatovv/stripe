"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from stripe_api.views import buy_router, item_router, order_new_router, order_buy_router, order_put_router, index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('buy/<item_id>', buy_router),
    path('item/<item_id>', item_router),
    path('order/buy/<order_id>', order_buy_router),
    path('order/put/<order_id>', order_put_router),
    path('order/new/', order_new_router),
]

