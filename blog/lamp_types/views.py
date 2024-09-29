from django.shortcuts import render, get_object_or_404
from .models import Type
from lamps.models import Lamp

def lamp_type(request, type_slug):
    lamp_type = get_object_or_404(Type, slug=type_slug)
    types = Type.objects.all()
    lamps = Lamp.objects.all()
    cont = {
        'lamp_type': lamp_type,
        'types': types,
        'lamps': lamps
    }
    return render(request, 'lamp_types/lamp_types.html', cont)
