from django.contrib import admin
from .models import Carcase, CarcasePlace

# Register your models here.

class PlacesInline(admin.TabularInline):
    model = CarcasePlace

class CarcaseAdmin(admin.ModelAdmin):
    fields = ['model', 'name', 'slug', 'year', 'image']
    inlines = [PlacesInline]

admin.site.register(Carcase, CarcaseAdmin)



