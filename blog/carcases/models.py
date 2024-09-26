from django.db import models
from models_autos.models import ModelAuto

# Create your models here.

class Carcase(models.Model):
    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE, default='', blank=True)
    name = models.CharField('Кузов', max_length=30, default='', blank=True)
    slug = models.SlugField(max_length=50, db_index=True, default='', blank=True)
    year = models.CharField('Год производства', max_length=30, default='', blank=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'carcase'
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузов'