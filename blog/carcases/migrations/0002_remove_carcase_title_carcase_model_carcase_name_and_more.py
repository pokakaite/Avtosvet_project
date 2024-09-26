# Generated by Django 5.0.9 on 2024-09-26 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carcases', '0001_initial'),
        ('models_autos', '0002_alter_modelauto_name_alter_modelauto_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carcase',
            name='title',
        ),
        migrations.AddField(
            model_name='carcase',
            name='model',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='models_autos.modelauto'),
        ),
        migrations.AddField(
            model_name='carcase',
            name='name',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Кузов'),
        ),
        migrations.AddField(
            model_name='carcase',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='carcase',
            name='year',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Год производства'),
        ),
    ]