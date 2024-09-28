from django.contrib import admin
from .models import Lamp, PlaceLamp

# Register your models here.

class PlaceInline(admin.TabularInline):
    model = PlaceLamp

class LampAdmin(admin.ModelAdmin):
    fields = ['title', 'voltage', 'base', 'type', 'watts', 'offset', 'length', 'color', 'brand', 'amount_type', 'price', 'image']
    inlines = [PlaceInline]

admin.site.register(Lamp, LampAdmin)


