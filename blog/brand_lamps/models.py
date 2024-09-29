from django.db import models

# Create your models here.

class BrandLamp(models.Model):
    name = models.CharField('Производитель', max_length=50, default='', blank=True)
    # name = models.CharField('Производитель', max_length=50, unique=True, db_index=True, blank=False)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'brand_lamp'
        verbose_name = 'Производителя ламп'
        verbose_name_plural = 'Производители ламп'