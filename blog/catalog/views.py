from django.shortcuts import render

# Create your views here.

def index(request):
    cont = {
        'main_title': 'Каталог'
    }
    return render(request, 'catalog/index.html', cont)