from django.shortcuts import render, get_object_or_404
from brand_autos.models import BrandAuto
from models_autos.models import ModelAuto
from carcases.models import Carcase
from places.models import Place
from .models import Type

# Create your views here.
def lamp_type(request, type_slug, carcase_slug, brand_slug):
    lamp_types = get_object_or_404(Type, slug=lamp_type)
    brand_autos = BrandAuto.objects.all()
    models_autos = ModelAuto.objects.all()
    places = Place.objects.all()
    for model in models_autos:
        for brand in brand_autos:
            if model.brand == brand.name:
                brand_slug = brand.slug
    cont = {
        'lamp_types': lamp_types,
        'main_title': 'Подбор ламп по авто',
        'brand_slug': brand_slug,
        'places': places
    }
    return render(request, 'carcases/carcase.html', cont)
    
