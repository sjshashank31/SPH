# Generated by Django 4.0 on 2022-02-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_product_product_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='units_available',
            new_name='stock_available',
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(blank=True, choices=[('KG', 'Kilogram'), ('G', 'Gram'), ('ML', 'Milli litre'), ('L', 'Litre')], max_length=2, null=True),
        ),
    ]
