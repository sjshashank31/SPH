# Generated by Django 4.0.3 on 2022-05-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_rename_code_inwardproduct_product_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='outwardproduct',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
