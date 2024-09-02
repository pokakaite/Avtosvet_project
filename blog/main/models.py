from django.db import models

# Create your models here.

class Brands(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка автомобиля')

    def __str__(self) -> str:
        return self.brand
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'brand'
        verbose_name = 'Марку автомобиля'
        verbose_name_plural = 'Марки автомобилей'

    
class ModelCars(models.Model):
    car_model = models.CharField('Модель автомобиля', max_length=50)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)

    class Meta:
        db_table: str = 'car_model'
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модель автомобиля'