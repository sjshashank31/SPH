# Generated by Django 4.0 on 2022-01-25 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_supervisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='labour',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.supervisor'),
        ),
    ]
