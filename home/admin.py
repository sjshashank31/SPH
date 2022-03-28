from django.contrib import admin
from .models import Payment, Product, Crop

# Register your models here.
admin.site.register(Payment)
admin.site.register(Crop)

admin.site.register(Product)

