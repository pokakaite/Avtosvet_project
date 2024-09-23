from django.urls import path
from .views import *

app_name = 'led'

urlpatterns = [
    path('', index, name='index')
]