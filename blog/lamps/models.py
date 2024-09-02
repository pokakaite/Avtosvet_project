from django.db import models

# Create your models here.

class Brand(models.Model):
    brand = models.CharField('Производитель', max_length=50)

class Category(models.Model):
    category = models.CharField('Категория', max_length=50)

class Lamps(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=50)
    volt = models.IntegerField('Вольтаж')
    watt = models.IntegerField('Мощность')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)