# Generated by Django 4.0 on 2022-01-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_labour_supervisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1080)),
                ('product_code', models.CharField(max_length=1080)),
                ('units_available', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
