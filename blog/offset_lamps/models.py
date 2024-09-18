from django.db import models

# Create your models here.

class Offset(models.Model):
    title = models.CharField('offset', max_length=50)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'offset'
        verbose_name = 'Смещение'
        verbose_name_plural = 'Смещение'