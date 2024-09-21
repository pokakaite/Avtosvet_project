from django.db import models

# Create your models here.

class LampBase(models.Model):
    name = models.CharField('Цоколь', max_length=10)
    watts = models.CharField('Мощность', max_length=10)