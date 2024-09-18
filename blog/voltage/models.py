from django.db import models

# Create your models here.

class Voltage(models.Model):
    title = models.CharField('Напряжение', max_length=4)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'voltage'
        verbose_name = 'Напряжение'
        verbose_name_plural = 'Напряжение'