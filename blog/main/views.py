from django.shortcuts import render
from brand_autos.models import BrandAuto
from lamps.models import Lamp

# Create your views here.

def index(request):
    brand_autos = BrandAuto.objects.order_by('name')
    cont = {
        'title': 'Главная',
        'main_title': 'Подбор ламп по авто',
        'brand_autos': brand_autos
    }
    return render(request, 'main/index.html', cont)

def payment(request):
    cont = {
        'main_title': 'Оплата и доставка'
    }
    return render(request, 'main/payment.html', cont)

def catalog(request):
    model = Lamp.objects.all()
    cont = {
        'types': {
            'Галогенные лампы': 1,
            'Светодиодные лампы': 2,
            'Ксеноновые лампы': 3
        },
        'Галогенные лампы': 'halogen',
        'Светодиодные лампы': 'led',
        'Ксеноновые лампы': 'xenon',
        'lamps': model
    }
    return render(request, 'main/catalog.html', cont)
