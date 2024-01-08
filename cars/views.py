from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Car


def cars_view(request):
    """
    cars = (Car.objects.all())  # Retorna todos os objetos do modelo Car
    fiat_cars = Car.objects.filter(brand__name="Fiat")  # Retorna todos os carros que tem a marca Fiat. O __ nos permite acessar a tabela relacionada Brand e seu campo name
    cars_with_c = Car.objects.filter(model__contains="C")  # Retorna todos os objetos de Car que contenham no model um C
    """
    cars = Car.objects.all()
    search = request.GET.get('search')  # Captura o valor de search passado pelo usário
    if search:
        cars = Car.objects.filter(model__contains=search)  # Retorna todos os objetos de Car que tenham no campo model o valor inserido em search pelo usuario
    #  request.GET  # Retorna todos os parametros passados pelo usuario em um QueryDict
    return render(
        request,
        'cars.html',
        {'cars': cars})

