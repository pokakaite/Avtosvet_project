from django.db import models
from brand_lamps.models import BrandLamp
from lamp_bases.models import LampBase
from voltage.models import Voltage
from lamp_types.models import Type 

# Create your models here.

class Lamp(models.Model):
    voltage = models.ForeignKey('Напряжение', Voltage, null=False)
    base = models.ForeignKey('Цоколь', LampBase, on_delete=models.CASCADE, null=False)
    type = models.ForeignKey('Тип лампы', Type, on_delete=models.CASCADE, null=False)
    brand = models.ForeignKey('Производитель', BrandLamp, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.base
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'lamp'
        verbose_name = 'Лампу'
        verbose_name_plural = 'Лампы'