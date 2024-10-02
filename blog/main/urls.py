from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('payment/', payment, name='payment'),
    path('catalog/', catalog, name='catalog'),
    path('cart/', cart, name='cart'),
    path('<slug:lamp_slug>/', lamps, name='lamps'),
]