# Generated by Django 5.0.9 on 2024-10-01 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lamps', '0002_lamp_in_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lamp',
            name='in_cart',
        ),
    ]