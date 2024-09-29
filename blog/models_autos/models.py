from django.db import models
from brand_autos.models import BrandAuto
# from places.models import Place

# Create your models here.

class ModelAuto(models.Model):
    brand = models.ForeignKey(BrandAuto, on_delete=models.CASCADE, verbose_name='Марка автомобиля')
    name = models.CharField(max_length=20, db_index=True, default='', blank=True)
    slug = models.SlugField(max_length=20, db_index=True, default='', blank=True)
    # brand = models.ForeignKey(BrandAuto, on_delete=models.CASCADE, verbose_name='Марка автомобиля')
    # name = models.CharField(max_length=20, db_index=True, unique=True, blank=False)
    # slug = models.SlugField(max_length=20, db_index=True, unique=True, blank=False)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'model'
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'