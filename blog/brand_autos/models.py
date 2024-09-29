from django.db import models
from django.urls import reverse

# Create your models here.

class BrandAuto(models.Model):
    name = models.CharField('Марка автомобиля', max_length=50, default='', blank=True)
    slug = models.SlugField(max_length=50, db_index=True, default='', blank=True)
    # name = models.CharField('Марка автомобиля', max_length=50, null=False, unique=True, db_index=True)
    # slug = models.SlugField(max_length=50, db_index=True, unique=True, blank=False)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('brand_autos:brand_auto', kwargs={'brand_slug': self.slug})
    
    class Meta:
        db_table: str = 'brand_auto'
        verbose_name = 'Марку автомобилей'
        verbose_name_plural = 'Марки автомобилей'