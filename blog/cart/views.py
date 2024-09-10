from django.shortcuts import render

# Create your views here.

def index(request):
    cont = {
        'main_title': 'Корзина'
    }
    return render(request, 'cart/index.html', cont)