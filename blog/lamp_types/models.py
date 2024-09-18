from django.db import models

# Create your models here.

class Type(models.Model):
    type = models.CharField('Тип лампы', max_length=50)

    def __str__(self) -> str:
        return self.type
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'type'
        verbose_name = 'Тип лампы'
        verbose_name_plural = 'Типы ламп'