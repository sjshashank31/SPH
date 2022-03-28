"""FarmProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('products/', views.get_products, name='products'),
    path('product_details/<id>/', views.get_product_details, name='product_details'),
    path('add_payment/', views.add_payment, name='add_payment'),
    path('add_crop/', views.add_payment, name='add_crop'),
    path('add_product/', views.add_payment, name='add_product'),
    path('update_payment/<str:bill_no>/', views.update_payment, name='update_payment'),
    path('payments/', views.get_payments, name='payments'),
    path('filter_payments_from_crop/<crop>/', views.filter_crop, name='filter_payments_from_crop'),


]
