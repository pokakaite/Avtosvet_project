from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('<slug:brand_slug>/', brand_auto, name='brand_auto')
]