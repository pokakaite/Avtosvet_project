from django.shortcuts import render, get_object_or_404
# from brand_autos.models import BrandAuto
# from models_autos.models import ModelAuto
# from carcases.models import Carcase
# from places.models import Place
from .models import Type
from lamps.models import Lamp
# from places.models import PlaceType

def lamp_type(request, type_slug):
    lamp_types = get_object_or_404(Type, slug=type_slug)
    lamps = Lamp.objects.all()
    cont = {
        'lamp_types': lamp_types,
        'lamps': lamps
    }
    return render(request, 'lamp_types/lamp_types.html', cont)

# Create your views here.
# def lamp_type(request, type_slug, carcase_slug, brand_slug):
#     lamp_types = get_object_or_404(Type, slug=lamp_type)
#     brand_autos = BrandAuto.objects.all()
#     models_autos = ModelAuto.objects.all()
#     # places_types = PlaceType.objects.all()
#     places = Place.objects.all()
#     for model in models_autos:
#         for brand in brand_autos:
#             if model.brand == brand.name:
#                 brand_slug = brand.slug
#     cont = {
#         'lamp_types': lamp_types,
#         'main_title': 'Подбор ламп по авто',
#         'brand_slug': brand_slug,
#         'places': places,
#         # 'places_types': places_types
#     }
#     return render(request, 'carcases/carcase.html', cont)
    
