# Generated by Django 5.0.7 on 2024-09-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200),
        ),
    ]