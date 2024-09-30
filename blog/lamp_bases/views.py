from django.shortcuts import render, get_object_or_404
from .models import LampBase, PlaceLamp
from brand_autos.models import BrandAuto
from models_autos.models import ModelAuto
from carcases.models import Carcase
from places.models import Place
from lamps.models import Lamp

# Create your views here.

def lamp_bases(request, carcase_slug, brand_slug, model_slug, lamp_base_slug):
    lamp_bases = get_object_or_404(LampBase, slug=lamp_base_slug)
    lamp_places = PlaceLamp.objects.all()
    carcases_obj = Carcase.objects.all()
    lamp_bases_obj = LampBase.objects.all()
    brand_autos = BrandAuto.objects.all()
    models_autos = ModelAuto.objects.all()
    places = Place.objects.all()
    lamps = Lamp.objects.all()

    for carcase in carcases_obj:
        for lamp_place in lamp_places:
            if lamp_place.carcase == carcase.name:
                carcase_slug == carcase.slug
        for model_auto in models_autos:
            if carcase.model == model_auto.name:
                model_slug == model_auto.slug
        for brand in brand_autos:
            if model_auto.brand == brand.name:
                brand_slug = brand.slug

        cont = {
        'title': 'Цоколь',
        'lamp_bases': lamp_bases,
        'lamp_bases_obj': lamp_bases_obj,
        'carcases_obj': carcases_obj,
        'brand_slug': brand_slug,
        'model_slug': model_slug,
        'carcase_slug': carcase_slug,
        'places': places,
        'lamp_places': lamp_places,
        'lamps': lamps,
        'error': None,
    }

    return render(request, 'lamp_bases/lamp_bases.html', cont)
