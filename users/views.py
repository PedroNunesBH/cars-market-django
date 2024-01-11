from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from cars.models import Brand
from django.contrib.auth.forms import UserCreationForm


def create_user(request):
    car_brands = Brand.objects.all()
    if request.method == "POST":
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('cars_list')
    else:
        user_creation_form = UserCreationForm()
    return render(request, 'create_user.html', {'car_brands': car_brands, 'user_creation_form': user_creation_form})