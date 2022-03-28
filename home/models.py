from django.utils import timezone
from django import forms
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Crop(models.Model):
    name = models.CharField(max_length=1080)
    start_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=200, null=True, blank=True, unique=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    volume = models.FloatField(default=0, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.code)


class Payment(models.Model):
    bill_no = models.CharField(max_length=100, blank=True, null=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    qty_used = models.FloatField(default=0)
    used_for = models.CharField(max_length=50, blank=True, null=True)
    payment_date = models.DateField(default=timezone.now)
    male_labour_used = models.IntegerField(default=0)
    female_labour_used = models.IntegerField(default=0)
    labour_amount = models.FloatField(default=0)
    petrol_amount = models.FloatField(default=0)
    diesel_amount = models.FloatField(default=0)
    total_amount = models.FloatField(default=0)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.bill_no)




