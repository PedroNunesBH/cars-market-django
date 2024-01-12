from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from cars.models import Brand
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def create_user(request):
    car_brands = Brand.objects.all()
    if request.method == "POST":
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('login_page')  # Redireciona para a pagina de login
    else:
        user_creation_form = UserCreationForm()
    return render(request, 'create_user.html', {'car_brands': car_brands, 'user_creation_form': user_creation_form})


def login_view(request):
    car_brands = Brand.objects.all()
    if request.method == "POST":
        username = request.POST['username']  # Captura o valor de username
        password = request.POST['password']  # Captura o valor de password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Realiza o login
            return redirect('cars_list')  # Redireciona o usuario para a pagina de name cars_list
        else:
            auth_form = AuthenticationForm()
    else:
        auth_form = AuthenticationForm()
    return render(request, "login.html", {'car_brands': car_brands, 'auth_form': auth_form})

def logout_view(request):
    car_brands = Brand.objects.all()
    return render(request, 'logout.html', {'car_brands': car_brands})