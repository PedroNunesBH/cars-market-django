from django.contrib import admin
from .models import Car, Brand

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')  # Campos que serão mostrados
    search_fields = ('model', 'brand')  # Campo(s) que serão usados para fazer busca


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
