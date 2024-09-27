from django.db import models
from lamp_types.models import Type

# Create your models here.

class Place(models.Model):
    place = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, db_index=True, default='', blank=True)
    image = models.ImageField(default='no_image.svg', upload_to='profiles', verbose_name='Изображение')

    def __str__(self) -> str:
        return self.place
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'place'
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class PlaceType(models.Model):
    place = models.ForeignKey(Place, related_name="type", on_delete=models.CASCADE)
    types = models.ForeignKey(Type, on_delete=models.CASCADE)

