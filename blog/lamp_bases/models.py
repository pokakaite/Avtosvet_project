from django.db import models
from lamp_types.models import Type
from carcases.models import Carcase
from places.models import Place
from django.urls import reverse

# Create your models here.

class LampBase(models.Model):
    name = models.CharField('Цоколь', max_length=20, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, default='', blank=True)
    watts = models.CharField('Мощность', max_length=10, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default='', blank=True, null=True)
    image = models.ImageField(default='no_image.svg', upload_to='lamp_bases', verbose_name='Изображение')

    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('lamp_bases:lamp_bases', kwargs={'lamp_base_slug': self.slug})
    
    class Meta:
        db_table: str = 'lamp_base'
        verbose_name = 'Цоколь'
        verbose_name_plural = 'Цоколь'

class PlaceLamp(models.Model):
    lamp_base = models.ForeignKey(LampBase, related_name="places", on_delete=models.CASCADE)
    places = models.ForeignKey(Place, on_delete=models.CASCADE)
    carcase = models.ForeignKey(Carcase, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default='', blank=True, null=True)