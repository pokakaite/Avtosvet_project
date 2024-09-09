from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    form = UserCreationForm()
    cont = {
        'form': form
    }
    return render(request, 'users/register.html', cont)