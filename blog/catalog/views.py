from django.shortcuts import render
from lamps.models import Lamp

# Create your views here.

def index(request):
    model = Lamp.objects.all()
    cont = {
        'main_title': 'Галогенные лампы',
        'led': 'Светодиодные лампы',
        'xenon': 'Ксеноновые лампы',
        'lamps': model
    }
    return render(request, 'catalog/index.html', cont)