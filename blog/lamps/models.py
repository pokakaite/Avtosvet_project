from django.db import models
from lamp_bases.models import LampBase
from voltage.models import Voltage
from lamp_types.models import Type
from offset_lamps.models import Offset
from length.models import Length
from brand_lamps.models import BrandLamp
from colors.models import Color
from amount_types.models import AmountType
from django.urls import reverse


# Create your models here.

class Lamp(models.Model):
    base = models.ForeignKey(LampBase, on_delete=models.CASCADE, null=False, default=None, verbose_name='Цоколь')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False, default=None, verbose_name='Тип лампы')
    voltage = models.ForeignKey(Voltage, on_delete=models.CASCADE, null=False, default=None, verbose_name='Напряжение')
    watts = models.CharField('Мощность/Люмены', max_length=10, null=True, blank=True)
    title = models.CharField('Описание', max_length=40, null=True, blank=True)
    slug = models.SlugField(max_length=50, db_index=True, default='', blank=True)
    offset = models.ForeignKey(Offset, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name='Смещение')
    length = models.ForeignKey(Length, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name='Длина')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name='Цвет')
    brand = models.ForeignKey(BrandLamp, on_delete=models.CASCADE, null=False, default=None, verbose_name='Производитель')
    amount_type = models.ForeignKey(AmountType, on_delete=models.CASCADE, null=True, default=None, verbose_name='Тип количества')
    price = models.IntegerField('Цена', null=True, default=0)
    image = models.ImageField(default='no_image.svg', upload_to='lamps', verbose_name='Изображение')

    def __str__(self) -> str:
        return f'Лампа {self.base} {self.voltage} {self.title}'
    
    def get_absolute_url(self):
        return reverse('lamps:lamps', kwargs={'lamp_slug': self.slug})
    
    class Meta:
        db_table: str = 'lamp'
        verbose_name = 'Лампу'
        verbose_name_plural = 'Лампы'