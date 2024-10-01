from django.shortcuts import render, get_object_or_404
from brand_autos.models import BrandAuto
from models_autos.models import ModelAuto
from carcases.models import Carcase
from places.models import Place
from lamp_types.models import Type
from lamps.models import Lamp
from .models import CarcasePlace
from lamp_bases.models import PlaceLamp, LampBase

# Create your views here.
def carcase(request, carcase_slug, brand_slug, model_slug):
    carcases = get_object_or_404(Carcase, slug=carcase_slug)
    carcases_obj = Carcase.objects.all()
    brand_autos = BrandAuto.objects.all()
    models_autos = ModelAuto.objects.all()
    places = Place.objects.order_by('slug')
    types = Type.objects.order_by('slug')
    lamps_places = PlaceLamp.objects.all()
    lamps = Lamp.objects.order_by('type')
    lamps_bases = LampBase.objects.all()
    carcases_places = CarcasePlace.objects.order_by('places')
    for model_auto in models_autos:
        for carcase in carcases_obj:
            if carcase.model == model_auto.name:
                model_slug = model_auto.slug
        for brand in brand_autos:
            if model_auto.brand == brand.name:
                brand_slug = brand.slug
    cont = {
        'carcases': carcases,
        'carcases_obj': carcases_obj,
        'title': 'Лампы для',
        'brand_slug': brand_slug,
        'model_slug': model_slug,
        'carcase_slug': carcase_slug,
        'places': places,
        'types': types,
        'lamps_places': lamps_places,
        'lamps': lamps,
        'carcases_places': carcases_places,
        'error': None,
        'lamps_bases': lamps_bases
    }
    return render(request, 'carcases/carcase.html', cont)
    
