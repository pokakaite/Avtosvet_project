from django.shortcuts import render
from .models import Brands

# Create your views here.

def index(request):
    brands = Brands.objects.order_by('brand')

    cont = {
        'title': 'Главная',
        'main_title': 'Подбор ламп по авто',
        'brands': brands
    }
    return render(request, 'main/index.html', cont)