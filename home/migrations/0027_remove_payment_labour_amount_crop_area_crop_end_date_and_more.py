# Generated by Django 4.0.3 on 2022-04-03 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0026_rename_labour_used_payment_female_labour_used_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='labour_amount',
        ),
        migrations.AddField(
            model_name='crop',
            name='area',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='crop',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='area',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='diesel_used',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='female_labour_paid_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='male_labour_paid_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='petrol_used',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='total_labour_amount',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='outward_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_outwarded', models.FloatField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='inward_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_added', models.FloatField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
