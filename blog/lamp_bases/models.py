from django.db import models
from lamp_types.models import Type
from carcases.models import Carcase
from places.models import Place

# Create your models here.

class LampBase(models.Model):
    name = models.CharField('Цоколь', max_length=20, db_index=True)
    watts = models.CharField('Мощность', max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'lamp_base'
        verbose_name = 'Цоколь'
        verbose_name_plural = 'Цоколь'

class PlaceLamp(models.Model):
    lamp_base = models.ForeignKey(LampBase, related_name="places", on_delete=models.CASCADE)
    places = models.ForeignKey(Place, on_delete=models.CASCADE)
    carcase = models.ForeignKey(Carcase, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default='', blank=True, null=True)
    # type = models.ForeignKey(Type, on_delete=models.CASCADE, unique=True, blank=False, null=False)
