from django.forms import ModelForm, RadioSelect
from .models import *

USED_FOR = (('Spray', 's'), ('Drip', 'd'), ('Spray & Drip', 'sd'))
PRODUCT_TYPE = (('L', 'Liquid'), ('S', 'Solid'), ('P', 'Powder'))


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'used_for': RadioSelect(choices=USED_FOR)
        }


class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_type': RadioSelect(choices=PRODUCT_TYPE),
        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class OutwardProductForm(ModelForm):
    class Meta:
        model = OutwardProduct
        fields = ['task', 'code', 'volume_outwarded', 'used_for']
        widgets = {
            'used_for': RadioSelect(choices=USED_FOR)
        }


class LabourForm(ModelForm):
    class Meta:
        model = Labour
        fields = '__all__'


class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
