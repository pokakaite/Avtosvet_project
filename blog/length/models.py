from django.db import models

# Create your models here.

class Length(models.Model):
    length = models.CharField('Длина', max_length=10)

    def __str__(self) -> str:
        return self.length
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'length'
        verbose_name = 'Длина'
        verbose_name_plural = 'Длина'