from django.shortcuts import render, get_object_or_404
from lamp_bases.models import LampBase
from brand_autos.models import BrandAuto
from models_autos.models import ModelAuto
from carcases.models import Carcase
from .models import Lamp

# Create your views here.

def lamps(request, carcase_slug, brand_slug, model_slug, lamp_base_slug, lamp_slug):
    lamp_main = get_object_or_404(Lamp, slug=lamp_slug)
    carcase_main = get_object_or_404(Carcase, slug=carcase_slug)
    brand_main = get_object_or_404(BrandAuto, slug=brand_slug)
    model_main = get_object_or_404(ModelAuto, slug=model_slug)
    lamp_base_main = get_object_or_404(LampBase, slug=lamp_base_slug)
    cont = {
        'lamp_main': lamp_main,
        'carcase_main': carcase_main,
        'brand_main': brand_main,
        'model_main': model_main,
        'lamp_base_main': lamp_base_main
    }
    return render(request, 'lamps/lamps.html', cont)


    