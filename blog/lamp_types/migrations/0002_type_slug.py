# Generated by Django 5.0.9 on 2024-09-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamp_types', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
