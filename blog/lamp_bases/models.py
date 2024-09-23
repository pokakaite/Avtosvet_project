from django.db import models

# Create your models here.

class LampBase(models.Model):
    name = models.CharField('Цоколь', max_length=10)
    watts = models.CharField('Мощность', max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'lamp_base'
        verbose_name = 'Цоколь'
        verbose_name_plural = 'Цоколь'