# Generated by Django 5.0.9 on 2024-10-01 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamp_bases', '0003_placelamp_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placelamp',
            name='lamp_base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='lamp_bases.lampbase'),
        ),
    ]
