from django.db import models
from django.urls import reverse

# Create your models here.

class BrandAuto(models.Model):
    name = models.CharField('Марка автомобиля', max_length=50, null=False, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:brand_auto', kwargs={'brand_slug': self.slug})
    
    class Meta:
        db_table: str = 'brand_auto'
        verbose_name = 'Марку автомобилей'
        verbose_name_plural = 'Марки автомобилей'