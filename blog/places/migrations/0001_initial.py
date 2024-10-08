# Generated by Django 5.0.9 on 2024-09-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, default='')),
                ('image', models.ImageField(default='no_image.svg', upload_to='places', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'db_table': 'place',
            },
        ),
    ]
