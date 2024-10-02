from django.shortcuts import render, get_object_or_404
from lamp_bases.models import LampBase
from lamps.models import Lamp
from brand_autos.models import BrandAuto
from lamps.models import Lamp
from users.models import User


# Create your views here.

def index(request):
    brand_autos = BrandAuto.objects.order_by('name')
    users = User.objects.all()
    cont = {
        'title': 'Главная',
        'main_title': 'Подбор ламп по авто',
        'brand_autos': brand_autos,
        'users': users
    }
    return render(request, 'main/index.html', cont)

def payment(request):
    cont = {
        'main_title': 'Оплата и доставка'
    }
    return render(request, 'main/payment.html', cont)

def catalog(request):
    model = Lamp.objects.order_by('-price')
    cont = {
        'types': {
            'Галогенные лампы': '2-halogen',
            'Светодиодные лампы': '3-led',
            'Лампы накаливания': '1-incandescent',
            'Штатные ксеноновые лампы': '4-xenon',
            'Нештатные ксеноновые лампы': '5-no-xenon',
        },
        'lamps': model,
    }
    return render(request, 'main/catalog.html', cont)

def cart(request):
    cont = {
        'main_title': 'Корзина'
    }
    return render(request, 'cart/cart.html', cont)

def lamps(request, lamp_slug):
    lamp_main = get_object_or_404(Lamp, slug=lamp_slug)
    cont = {
        'lamp_main': lamp_main,
    }
    return render(request, 'lamps/lamps.html', cont)

