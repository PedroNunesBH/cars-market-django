# Generated by Django 5.0.1 on 2024-01-12 18:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_car_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='day_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, null=True),
        ),
    ]
