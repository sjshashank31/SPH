from django.forms import ModelForm, RadioSelect
from .models import *

USED_FOR = (('Spray', 's'), ('Drip', 'd'), ('Spray & Drip', 'sd'))


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'used_for': RadioSelect(choices=USED_FOR)
        }

