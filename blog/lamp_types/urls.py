from django.urls import path
from .views import *

app_name = 'lamp_types'

urlpatterns = [
    path('<slug:lamp_type>/', lamp_type, name='lamp_type'),
]