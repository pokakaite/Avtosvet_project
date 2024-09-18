from django.db import models

# Create your models here.

class Carcase(models.Model):
    title = models.CharField('Кузов', max_length=30)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'carcase'
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузов'