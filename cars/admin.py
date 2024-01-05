from django.contrib import admin
from .models import Car, Brand

# Register your models here.


class CarAdmin(admin.ModelAdmin):  # Criacao de uma classe para registro do model Car no admin
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')  # Campos que serão mostrados
    search_fields = ('model', 'brand')  # Campo(s) que serão usados para fazer busca


class BrandAdmin(admin.ModelAdmin):  # Criacao da classe responsavel pelo registro do model Brand no admin
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Car, CarAdmin)  # Registro de Car no admin
admin.site.register(Brand, BrandAdmin)  # Registro de Brand no admin
