# Generated by Django 5.0.9 on 2024-09-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Тип лампы')),
                ('slug', models.SlugField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'Тип лампы',
                'verbose_name_plural': 'Типы ламп',
                'db_table': 'type',
            },
        ),
    ]
