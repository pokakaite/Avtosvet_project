from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('profile/', profile, name='profile')
]