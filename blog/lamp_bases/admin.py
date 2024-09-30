from django.contrib import admin
from .models import LampBase, PlaceLamp

# Register your models here.

class PlaceInline(admin.TabularInline):
    model = PlaceLamp

class LampAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'watts', 'image']
    inlines = [PlaceInline]

admin.site.register(LampBase, LampAdmin)
