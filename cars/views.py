from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Car, Brand
from cars.forms import RegisterNewCarByUserForm


def cars_view(request):
    """
    cars = (Car.objects.all())  # Retorna todos os objetos do modelo Car
    fiat_cars = Car.objects.filter(brand__name="Fiat")  # Retorna todos os carros que tem a marca Fiat. O __ nos permite acessar a tabela relacionada Brand e seu campo name
    cars_with_c = Car.objects.filter(model__contains="C")  # Retorna todos os objetos de Car que contenham no model um C
    cars = Car.objects.filter(model__contains=search) # Tem a mesma função do contains porem no case sensitive
    """
    car_brands = Brand.objects.all()
    cars = Car.objects.all().order_by('model')  # retorna todos os objetos do modelo Car ordenados em ordem alfabetica pelo campo model
    search = request.GET.get('search')  # Captura o valor de search passado pelo usário
    if search:
        cars = Car.objects.filter(model__contains=search)  # Retorna todos os objetos de Car que tenham no campo model o valor inserido em search pelo usuario
    #  request.GET  # Retorna todos os parametros passados pelo usuario em um QueryDict
    return render(
        request,
        'cars.html',
        {'cars': cars, 'car_brands': car_brands})


def user_register_new_car(request):
    car_brands = Brand.objects.all()  # Retornando uma Query Set com todas as marcas para acesso no html
    if request.method == "POST":  # request.method permite verificar qwual metodo esta sendo utilizado na request
        form_to_register_new_car_by_user = RegisterNewCarByUserForm(request.POST, request.FILES)  # Recebendo os dados e arquivos preenchidos
        if form_to_register_new_car_by_user.is_valid():  # Verificando se é valido
            new_car = form_to_register_new_car_by_user.save(
                commit=False)  # Salva o objeto do formulário, mas não persiste no banco de dados ainda
            new_car.autor = request.user  # Associa o usuário atual ao novo carro
            new_car.save()  # Agora salva o objeto no banco de dados
            return redirect('cars_list')
    else:
        form_to_register_new_car_by_user = RegisterNewCarByUserForm()
    return render(request, 'user_register_car.html', {'car_brands': car_brands, "form_to_register_new_car_by_user":  form_to_register_new_car_by_user})


def cars_user(request):
    car_brands = Brand.objects.all()
    user_id = request.user.id  # Capturando o id do user
    cars_by_user = Car.objects.filter(autor_id=user_id)  # Filtrando os carros que foram registrados(autor) pelo user
    return render(request, 'user_cars.html', {'car_brands': car_brands, 'cars_by_user': cars_by_user})