from django.urls import path
from .views import *

app_name = 'carcases'

urlpatterns = [
    path('<slug:model_slug>/<slug:carcase_slug>', carcase, name='carcase')
]