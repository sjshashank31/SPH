# Generated by Django 4.0.3 on 2022-05-10 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_alter_labour_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labour',
            name='task',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.task'),
        ),
    ]
