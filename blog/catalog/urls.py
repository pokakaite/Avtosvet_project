from django.urls import path
from .views import *

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index')
]