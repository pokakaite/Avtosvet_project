# Generated by Django 5.0.9 on 2024-09-28 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('models_autos', '0002_alter_modelauto_name_alter_modelauto_slug'),
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30, verbose_name='Кузов')),
                ('slug', models.SlugField(blank=True, default='')),
                ('year', models.CharField(blank=True, default='', max_length=30, verbose_name='Год производства')),
                ('image', models.ImageField(default='no_image.svg', upload_to='profiles', verbose_name='Изображение')),
                ('model', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='models_autos.modelauto')),
            ],
            options={
                'verbose_name': 'Кузов',
                'verbose_name_plural': 'Кузов',
                'db_table': 'carcase',
            },
        ),
        migrations.CreateModel(
            name='CarcasePlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='carcases.carcase')),
                ('places', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place')),
            ],
        ),
    ]
