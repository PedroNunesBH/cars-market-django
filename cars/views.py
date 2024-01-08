from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Car


def cars_view(request):
    cars = Car.objects.all()  # Retorna todos os objetos do modelo Car

    return render(
        request,
        'cars.html',
        {'cars': cars})

