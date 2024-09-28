from django.urls import path
from .views import *

app_name = 'lamp_types'

urlpatterns = [
    path('', lamp_type, name='lamp_type'),
]