# Generated by Django 4.0.3 on 2022-04-04 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0029_rename_area_crop_crop_area_remove_crop_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='crop_name',
            field=models.CharField(blank=True, max_length=1080, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
