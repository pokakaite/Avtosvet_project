"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from users.views import register as user_register
# from profiles.views import profile as user_profile


urlpatterns = [
    path('bruh/', admin.site.urls, name='bruh'),
    path('', include('main.urls', namespace='main')),
    path('brands_autos/', include('brand_autos.urls', namespace='brand_autos')),
    path('brands_autos/<slug:brand_slug>/', include('carcases.urls', namespace='carcases')),
    path('brands_autos/<slug:brand_slug>/', include('lamp_bases.urls', namespace='lamp_bases')),
    path('brands_autos/<slug:brand_slug>/', include('lamps.urls', namespace='lamps')),
    path('user/', include('users.urls', namespace='users')),
    path('catalog/<slug:type_slug>/', include('lamp_types.urls', namespace='lamp_types')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('user/register/', user_register, name='register'),
    path('user/register/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/', include('profiles.urls', namespace='profiles')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# from django.contrib.auth import views as auth_views
# from users.views import register as user_register
# from profiles.views import profile as user_profile
# from users.models import router, routers
# from users.models import UserViewSet
# from books.models import BookViewSet



# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'books', BookViewSet)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('main.urls')),
#     path('user/register/', user_register, name='register'),
#     path('user/register/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
#     path('accounts/profile/', user_profile, name='profile'),
#     # path('api/auth/', include('rest_framework.urls')),
#     # path('api/v1/', include(router.urls))
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
