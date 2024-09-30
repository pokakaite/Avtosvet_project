from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username', '')
            messages.success(request, f'{username}, Вы успешно зарегистрировались!')
            redirect('login/')
        else:
            messages.warning(request, 'Неправильно')
    else:
        form = UserRegisterForm()
    cont = {
        'form': form,
        'main_title': 'Вход или Регистрация'
    }
    return render(request, 'users/register.html', cont)
