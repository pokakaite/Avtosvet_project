from django.shortcuts import render

# Create your views here.

def cart(request):
    cont = {
        'main_title': 'Корзина'
    }
    return render(request, 'cart/cart.html', cont)