from django.db import models
from users.models import User
from lamps.models import Lamp
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lamp = models.ForeignKey(Lamp, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Корзина для {self.user.username} | Лампа {self.lamp.base} {self.lamp.title}'