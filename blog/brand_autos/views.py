from django.shortcuts import render, get_object_or_404
from brand_autos.models import BrandAuto
from models_autos.models import ModelAuto
from carcases.models import Carcase

# Create your views here.

def brand_auto(request, brand_slug):
    brand_autos = get_object_or_404(BrandAuto, slug=brand_slug)
    models_autos = ModelAuto.objects.all()
    carcases = Carcase.objects.all()
    
    cont = {
        'brand_autos': brand_autos,
        'main_title': 'Подбор ламп по авто',
        'models_autos': models_autos,
        'carcases': carcases,
    }
    return render(request, 'brand_autos/brand_auto.html', cont)