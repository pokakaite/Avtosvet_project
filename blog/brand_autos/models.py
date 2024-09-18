from django.db import models

# Create your models here.

class BrandAuto(models.Model):
    name = models.CharField('Марка автомобиля', max_length=50, null=False, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'brand_auto'
        verbose_name = 'Марку автомобилей'
        verbose_name_plural = 'Марки автомобилей'