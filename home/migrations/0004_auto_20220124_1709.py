# Generated by Django 3.0 on 2022-01-24 11:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220124_1510'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payments',
            new_name='Payment',
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 24, 11, 39, 46, 811328, tzinfo=utc)),
        ),
    ]
