from django.db import models

# Create your models here.

class Place(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.place
    
    def get_absolute_url(self):
        return 
    
    class Meta:
        db_table: str = 'model'
        verbose_name = 'Место'
        verbose_name_plural = 'Места'