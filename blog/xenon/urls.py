from django.urls import path
from .views import *

app_name = 'xenon'

urlpatterns = [
    path('', index, name='index')
]