from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from cars.models import Brand


def create_user(request):
    car_brands = Brand.objects.all()
    return render(request, 'create_user.html', {'car_brands': car_brands})