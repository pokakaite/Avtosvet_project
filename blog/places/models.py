from django.db import models

# Create your models here.

class Place(models.Model):
    place = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, db_index=True, default='', blank=True)

    def __str__(self) -> str:
        return self.place
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'place'
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

