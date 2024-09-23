from django.db import models
from brand_autos.models import BrandAuto
from lamps.models import Lamp
from places.models import Place

# Create your models here.

class ModelAuto(models.Model):
    brand = models.ForeignKey(BrandAuto, on_delete=models.CASCADE, verbose_name='Марка автомобиля')
    name = models.CharField(max_length=20)
    carcase = models.CharField(max_length=30)
    year = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name} {self.carcase} {self.year}'
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'model'
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'