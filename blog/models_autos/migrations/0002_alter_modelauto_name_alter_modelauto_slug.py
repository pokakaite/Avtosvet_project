# Generated by Django 5.0.9 on 2024-09-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_autos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelauto',
            name='name',
            field=models.CharField(db_index=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='modelauto',
            name='slug',
            field=models.SlugField(max_length=20, unique=True),
        ),
    ]