from django.urls import path
from .views import *

app_name = 'lamp_bases'

urlpatterns = [
    path('<slug:model_slug>/<slug:carcase_slug>/<slug:lamp_base_slug>', lamp_bases, name='lamp_bases')
]