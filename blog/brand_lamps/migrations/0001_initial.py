# Generated by Django 5.0.9 on 2024-09-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandLamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Производителя ламп',
                'verbose_name_plural': 'Производители ламп',
                'db_table': 'brand_lamp',
            },
        ),
    ]