# Generated by Django 5.0.9 on 2024-09-22 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voltage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4, verbose_name='Напряжение')),
            ],
            options={
                'verbose_name': 'Напряжение',
                'verbose_name_plural': 'Напряжение',
                'db_table': 'voltage',
            },
        ),
    ]
