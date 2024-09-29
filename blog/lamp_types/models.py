from django.db import models
from django.urls import reverse

# Create your models here.

class Type(models.Model):
    type = models.CharField('Тип лампы', max_length=50)
    slug = models.SlugField(max_length=50, db_index=True, default='', blank=True)
    # slug = models.SlugField(max_length=50, db_index=True, unique=True, blank=False)

    def __str__(self) -> str:
        return f'{self.type}'
    
    def get_absolute_url(self):
        return reverse('lamp_types:lamp_type', kwargs={'type_slug': self.slug})
    
    class Meta:
        db_table: str = 'type'
        verbose_name = 'Тип лампы'
        verbose_name_plural = 'Типы ламп'