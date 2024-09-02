# Generated by Django 5.0.7 on 2024-09-02 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Марка автомобиля')),
            ],
            options={
                'verbose_name': 'Марку автомобиля',
                'verbose_name_plural': 'Марки автомобилей',
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='ModelCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=50, verbose_name='Модель автомобиля')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brands')),
            ],
            options={
                'verbose_name': 'Модель автомобиля',
                'verbose_name_plural': 'Модель автомобиля',
                'db_table': 'car_model',
            },
        ),
    ]
