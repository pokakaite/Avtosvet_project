from django.shortcuts import render
from lamps.models import Lamp

# Create your views here.

def index(request):
    model = Lamp.objects.all()
    cont = {
        'types': {
            'Светодиодные лампы': 2},
        'lamps': model
    }
    return render(request, 'catalog/index.html', cont)