# Generated by Django 4.0 on 2022-02-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_remove_product_countinstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='total_amount',
            field=models.FloatField(default=0),
        ),
    ]