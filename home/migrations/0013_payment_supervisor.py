# Generated by Django 4.0 on 2022-01-28 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_amount_payment_total_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.supervisor'),
        ),
    ]
