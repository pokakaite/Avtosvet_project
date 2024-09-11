from django.urls import path, include
from .views import *

app_name = 'users'

urlpatterns = [
    path('register', index, name='register')
]