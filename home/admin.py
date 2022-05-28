from django.contrib import admin
from .models import Payment, Product, Crop, ProductCategory, Task, OutwardProduct, Labour

# Register your models here.
admin.site.register(Labour)
admin.site.register(Payment)
admin.site.register(Crop)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Task)
admin.site.register(OutwardProduct)

