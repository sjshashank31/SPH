from django.utils import timezone
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings
import itertools
import random
import string


# Create your models here.


class Crop(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    crop_name = models.CharField(max_length=1080, null=True, unique=True, blank=True)
    crop_area = models.FloatField(default=0)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.crop_name)

    def _generate_slug(self):
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        value = f"{self.crop_name} | S: {str(self.start_date)} | E: {str(self.end_date)}"
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Crop.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def get_slug(self):
        return self.slug

    def slug_save(self, *args, **kwargs):
        self._generate_slug()
        super().save(*args, **kwargs)


class ProductCategory(models.Model):
    product_category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.product_category


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=1080)
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product_code = models.CharField(max_length=200, null=True, blank=True, unique=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    product_type = models.CharField(max_length=2, blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)
    volume = models.FloatField(default=0, null=True, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.product_code)

    def add_product(self, *args, **kwargs):
        product_code = Product.objects.get(product_code=self.product_code)
        inward_product = InwardProduct(user=self.user, product_code=product_code, volume_added=self.volume,
                                       total_price=self.price,
                                       created_at=self.created_at)
        inward_product.save()


class InwardProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_code = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    volume_added = models.FloatField(default=0, null=True, blank=True)
    total_price = models.FloatField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class OutwardProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    code = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    volume_outwarded = models.FloatField(default=0, null=True, blank=True)
    used_for = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(default=0, null=True, blank=True)
    used_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def update_stock(self, *args, **kwargs):
        product = Product.objects.get(product_code=self.code)
        price_per_unit = product.volume/product.price
        product.volume = product.volume - self.volume_outwarded
        product.price = product.volume*price_per_unit
        product.save()
        super().save(*args, **kwargs)


class Payment(models.Model):
    bill_no = models.CharField(max_length=100, blank=True, null=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True, blank=True)
    area = models.FloatField(default=0)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    qty_used = models.FloatField(default=0)
    used_for = models.CharField(max_length=50, blank=True, null=True)
    payment_date = models.DateField(default=timezone.now)
    male_labour_used = models.IntegerField(default=0)
    female_labour_used = models.IntegerField(default=0)
    male_labour_paid_amount = models.FloatField(default=0)
    female_labour_paid_amount = models.FloatField(default=0)
    total_labour_amount = models.FloatField(default=0)
    petrol_used = models.FloatField(default=0)
    diesel_used = models.FloatField(default=0)
    petrol_amount = models.FloatField(default=0)
    diesel_amount = models.FloatField(default=0)
    total_amount = models.FloatField(default=0)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.bill_no)


class Labour(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    task = models.OneToOneField(Task, on_delete=models.SET_NULL, null=True, blank=True)
    male_count = models.IntegerField(default=0, blank=True, null=True)
    female_count = models.IntegerField(default=0, blank=True, null=True)
    male_amount = models.FloatField(blank=True)
    female_amount = models.FloatField(blank=True)
    date = models.DateField(auto_now_add=True)

    def save_data(self, *args, **kwargs):
        self.male_amount = (self.male_count)*250
        self.female_amount = (self.female_count)*(200)
        super().save(*args, **kwargs)
