from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            messages.success(request, f'{username}, Вы успешно зарегистрировались!')
            # cteates user
            redirect('login/')
        else:
            messages.warning(request, 'Неправильно')
    else:
        form = UserCreationForm()
    cont = {
        'form': form,
        'main_title': 'Вход или Регистрация'
    }
    return render(request, 'users/index.html', cont)
