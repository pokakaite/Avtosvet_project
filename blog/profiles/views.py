from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from cart.models import Cart
from .models import Profile

# Create your views here.

@login_required
def profile(request):
    cont = {
        # 'carts': Cart.objects.all(),
        'main_title': 'Профиль'
    }
    return render(request, 'profiles/profile.html', cont)