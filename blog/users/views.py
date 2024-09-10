from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    form = UserCreationForm()
    cont = {
        'form': form,
        'main_title': 'Вход или Регистрация'
    }
    return render(request, 'users/index.html', cont)