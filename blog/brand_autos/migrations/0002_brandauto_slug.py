# Generated by Django 5.0.9 on 2024-09-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_autos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandauto',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]