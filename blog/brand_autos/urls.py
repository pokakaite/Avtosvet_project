from django.urls import path
from .views import *

app_name = 'brand_autos'

urlpatterns = [
    path('<slug:brand_slug>/', brand_auto, name='brand_auto'),
]