# Generated by Django 5.0.1 on 2024-01-05 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brands'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brands',
            new_name='Brand',
        ),
    ]
