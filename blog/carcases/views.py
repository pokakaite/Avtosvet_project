from django.shortcuts import render, get_object_or_404
from brand_autos.models import BrandAuto
from models_autos.models import ModelAuto
from carcases.models import Carcase

# Create your views here.
def carcase(request, carcase_slug, brand_slug):
    carcases = get_object_or_404(Carcase, slug=carcase_slug)
    brand_autos = BrandAuto.objects.all()
    models_autos = ModelAuto.objects.all()
    for model in models_autos:
        for brand in brand_autos:
            if model.brand == brand.name:
                brand_slug = brand.slug
    cont = {
        'carcases': carcases,
        'choose_model': 'Модели автомобиля',
        'brand_slug': brand_slug
    }
    return render(request, 'carcases/carcase.html', cont)
    
