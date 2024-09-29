from django.db import models

# Create your models here.

class AmountType(models.Model):
    type = models.CharField('Тип количества', max_length=10, default='', blank=False)
    # type = models.CharField('Тип количества', max_length=10, unique=True, db_index=True, blank=False)

    def __str__(self) -> str:
        return self.type
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'amount'
        verbose_name = 'Тип количества'
        verbose_name_plural = 'Типы количества'