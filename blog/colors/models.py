from django.db import models

# Create your models here.

class Color(models.Model):
    color = models.CharField('Цвет', max_length=30)

    def __str__(self) -> str:
        return self.color
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'color'
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'