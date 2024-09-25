from django.shortcuts import render
from lamps.models import Lamp

# Create your views here.

def index(request):
    model = Lamp.objects.all()
    cont = {
        'types': {
            'Галогенные лампы': 1,
            'Светодиодные лампы': 2,
            'Ксеноновые лампы': 3
        },
        'Галогенные лампы': 'halogen',
        'Светодиодные лампы': 'led',
        'Ксеноновые лампы': 'xenon',
        'lamps': model
    }
    return render(request, 'catalog/index.html', cont)