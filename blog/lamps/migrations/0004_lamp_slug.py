# Generated by Django 5.0.9 on 2024-10-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamps', '0003_remove_lamp_in_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='lamp',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
