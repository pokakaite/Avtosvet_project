from django.db import models

# Create your models here.

class AmountType(models.Model):
    title = models.CharField('Тип количества', max_length=10)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'amount'
        verbose_name = 'Тип количества'
        verbose_name_plural = 'Типы количества'