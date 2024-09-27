from django.shortcuts import render, get_object_or_404
from brand_autos.models import BrandAuto
from models_autos.models import ModelAuto
from carcases.models import Carcase
from places.models import Place, PlaceType
from lamp_types.models import Type
from .models import CarcasePlace

# Create your views here.
def carcase(request, carcase_slug, brand_slug, model_slug):
    carcases = get_object_or_404(Carcase, slug=carcase_slug)
    carcases_obj = Carcase.objects.all()
    brand_autos = BrandAuto.objects.all()
    models_autos = ModelAuto.objects.all()
    places = Place.objects.all()
    types = Type.objects.all()
    places_types = PlaceType.objects.all()
    carcases_places = CarcasePlace.objects.all()
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
        'main_title': 'Подбор ламп по авто',
        'brand_slug': brand_slug,
        'model_slug': model_slug,
        'places': places,
        'types': types,
        'places_types': places_types,
        'carcases_places': carcases_places
    }
    return render(request, 'carcases/carcase.html', cont)
    
