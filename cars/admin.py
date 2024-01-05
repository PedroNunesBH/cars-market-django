from django.contrib import admin
from .models import Car

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')  # Campos que serão mostrados
    search_fields = ('model', 'brand')  # Campo(s) que serão usados para fazer busca


admin.site.register(Car, CarAdmin)
