# Generated by Django 5.0.9 on 2024-09-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='amount')),
            ],
            options={
                'verbose_name': 'Количество',
                'verbose_name_plural': 'Количество',
                'db_table': 'amount',
            },
        ),
    ]
