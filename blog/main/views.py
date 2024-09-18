from django.shortcuts import render
from brand_autos.models import BrandAuto

# Create your views here.

def index(request):
    brand_autos = BrandAuto.objects.order_by('name')

    cont = {
        'title': 'Главная',
        'main_title': 'Подбор ламп по авто',
        'brand_autos': brand_autos
    }
    return render(request, 'main/index.html', cont)