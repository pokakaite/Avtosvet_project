# Generated by Django 5.0.9 on 2024-09-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_autos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandauto',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Марка автомобиля'),
        ),
    ]