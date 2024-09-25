from django.shortcuts import render
from lamps.models import Lamp

# Create your views here.

def index(request):
    model = Lamp.objects.all()
    cont = {
        'types': {
            'Галогенные лампы': 1},
        'lamps': model,
    }
    return render(request, 'catalog/index.html', cont)