# Generated by Django 5.0.1 on 2024-01-17 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_remove_car_status_car_allowed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='allowed',
        ),
    ]
