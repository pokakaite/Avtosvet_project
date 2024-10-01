from django.shortcuts import render, get_object_or_404
from .models import LampBase, PlaceLamp
from brand_autos.models import BrandAuto
from models_autos.models import ModelAuto
from carcases.models import Carcase, CarcasePlace
from places.models import Place
from lamps.models import Lamp
from lamp_types.models import Type

# Create your views here.

def lamp_bases(request, carcase_slug, brand_slug, model_slug, lamp_base_slug):
    lamp_base_main = get_object_or_404(LampBase, slug=lamp_base_slug)
    carcase_main = get_object_or_404(Carcase, slug=carcase_slug)
    brand_main = get_object_or_404(BrandAuto, slug=brand_slug)
    model_main = get_object_or_404(ModelAuto, slug=model_slug)
    lamp_places = PlaceLamp.objects.all()
    carcases_obj = Carcase.objects.all()
    lamp_bases = LampBase.objects.all()
    brand_autos = BrandAuto.objects.all()
    models_autos = ModelAuto.objects.all()
    places = Place.objects.all()
    lamps = Lamp.objects.order_by('price')
    lamp_types = Type.objects.all()
    carcase_places = CarcasePlace.objects.all()

    cont = {
        'title': 'Цоколь',
        'lamp_base_main': lamp_base_main,
        'lamp_bases': lamp_bases,
        'carcases_obj': carcases_obj,
        'brand_slug': brand_slug,
        'model_slug': model_slug,
        'carcase_slug': carcase_slug,
        'places': places,
        'lamp_places': lamp_places,
        'lamps': lamps,
        'lamp_types': lamp_types,
        'carcase_places': carcase_places,
        'carcase_main': carcase_main,
        'carcase_main': carcase_main,
        'brand_main': brand_main,
        'model_main': model_main,
        'lamp_base_main': lamp_base_main
    }

    return render(request, 'lamp_bases/lamp_bases.html', cont)
