from django.urls import path
from .views import *

app_name = 'halogen'

urlpatterns = [
    path('', index, name='index')
]