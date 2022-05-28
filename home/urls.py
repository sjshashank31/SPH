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
    path('add_crop/', views.add_crop, name='add_crop'),
    path('crops/', views.get_crops, name='crops'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_task/', views.add_task, name='add_task'),
    path('tasks/', views.get_tasks_list, name='task_list'),
    path('update_task/<id>/', views.update_task, name='update_task'),
    path('used_product/', views.used_product, name='used_product'),
    path('inward_products/', views.get_inward_products, name='inward_products'),
    path('used_products_list/', views.get_used_products, name='used_products'),
    path('add_labours/', views.add_labour, name='add_labour'),
    path('labour_payments/', views.labour_details, name='labour_payments'),
    path('product_category_form/', views.add_product_category, name='add_product_category'),
    path('product_categories/', views.product_categories, name='product_categories'),
    path('expenses/<id>/', views.expenses, name='expenses')


]
