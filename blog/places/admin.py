from django.contrib import admin
from .models import Place, PlaceType

# Register your models here.

class TypesInline(admin.TabularInline):
    model = PlaceType

class PlaceAdmin(admin.ModelAdmin):
    fields = ['place', 'slug']
    inlines = [TypesInline]

admin.site.register(Place, PlaceAdmin)



