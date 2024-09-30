from django.db import models
from models_autos.models import ModelAuto
from places.models import Place
from django.urls import reverse

# Create your models here.

class Carcase(models.Model):
    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE, default='', blank=True)
    name = models.CharField('Кузов', max_length=30, default='', blank=True)
    slug = models.SlugField(max_length=50, db_index=True, default='', blank=True)
    year = models.CharField('Год производства', max_length=30, default='', blank=True)

    # model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE, default='', blank=False, null=False)
    # name = models.CharField('Кузов', max_length=30, default='', blank=True)
    # slug = models.SlugField(max_length=50, db_index=True, default='', blank=True)
    # year = models.CharField('Год производства', max_length=30, blank=False, null=False)
    image = models.ImageField(default='no_image.svg', upload_to='carcases', verbose_name='Изображение')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('carcases:carcase', kwargs={'carcase_slug': self.slug})
    
    class Meta:
        db_table: str = 'carcase'
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузов'

class CarcasePlace(models.Model):
    carcase = models.ForeignKey(Carcase, related_name="places", on_delete=models.CASCADE)
    places = models.ForeignKey(Place, on_delete=models.CASCADE)