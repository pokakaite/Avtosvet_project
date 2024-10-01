from django.urls import path
from .views import *

app_name = 'lamps'

urlpatterns = [
    path('<slug:model_slug>/<slug:carcase_slug>/<slug:lamp_base_slug>/<slug:lamp_slug>', lamps, name='lamps')
]