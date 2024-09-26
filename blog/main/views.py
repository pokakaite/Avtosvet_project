from django.shortcuts import render, get_object_or_404
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

def brand_auto(request, brand_slug):
    brand_autos = get_object_or_404(BrandAuto, slug=brand_slug)
    cont = {
        'brand_autos': brand_autos,
        'choose_model': 'Модели автомобиля',
    }
    return render(request, 'main/brand_auto.html', cont)
