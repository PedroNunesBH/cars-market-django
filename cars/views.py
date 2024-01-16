from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView, UpdateView, DeleteView
from .models import Car, Brand
from cars.forms import RegisterNewCarByUserForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

"""
def cars_view(request):
    cars = (Car.objects.all())  # Retorna todos os objetos do modelo Car
    fiat_cars = Car.objects.filter(brand__name="Fiat")  # Retorna todos os carros que tem a marca Fiat. O __ nos permite acessar a tabela relacionada Brand e seu campo name
    cars_with_c = Car.objects.filter(model__contains="C")  # Retorna todos os objetos de Car que contenham no model um C
    cars = Car.objects.filter(model__contains=search) # Tem a mesma função do contains porem no case sensitive
------------------------------------------------------------------------------------------------------
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
"""


class CarView(ListView):
    model = Car
    template_name = 'cars.html'


    def get_context_data(self, **kwargs): # Metodo para criar e acessar contextos
        context = super().get_context_data(**kwargs)
        context["car_brands"] = Brand.objects.all()  # Criando contexto 'car_brands'
        return context

    def get_queryset(self):  # Metodo utilizado para retornar o QuerySet
        queryset = super().get_queryset().order_by('model')  # Configura a query set do metodo da classe pai para ser ordenado pelo model (Car.objects.all().order_by('model)
        search = self.request.GET.get('search', '')  # Captura o valor de search
        queryset = Car.objects.filter(Q(model__icontains=search) | Q(brand__name__icontains=search))  # Retorna os carros que contem a 'search' em seu modelo ou em sua brand name relacionada !
        return queryset

"""
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
"""


@method_decorator(login_required(login_url='/login/'), name='dispatch')  # Adiciona um decorador para o methodo dispatch
class UserRegisterNewCar(CreateView):  # A create view é utilizada para as CBV's que a principal finalidade é criar objetos em um BD
    model = Car  # Modelo que será criado os objetos
    form_class = RegisterNewCarByUserForm  # Formulario responsavel pela criação do objeto
    template_name = 'user_register_car.html'
    success_url = reverse_lazy('cars_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['car_brands'] = Brand.objects.all()
        return context


"""
def cars_user(request):
    car_brands = Brand.objects.all()
    user_id = request.user.id  # Capturando o id do user
    cars_by_user = Car.objects.filter(autor_id=user_id)  # Filtrando os carros que foram registrados(autor) pelo user
    return render(request, 'user_cars.html', {'car_brands': car_brands, 'cars_by_user': cars_by_user})
"""


@method_decorator(login_required, name='dispatch')
class CarsUser(ListView):
    model = Car  # Modelo que a listview é associada
    template_name = 'user_cars.html'  # Template que sera renderizado

    def get_context_data(self, **kwargs):  # Metodo para editar contextos
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id  # Capturando o id do usuario
        context['cars_by_user'] = Car.objects.filter(autor_id=user_id)  # Criando o contexto cars_by_user que são os objetos do model Car que tem como autor o usuario
        context['car_brands'] = Brand.objects.all()
        return context


class DetailCar(DetailView):
    model = Car
    template_name = 'detail_car.html'

    def get(self, request, *args, **kwargs):
        car = self.get_object()  # Capturando qual o carro da detail view
        car.views_by_user += 1  # Incrementando em views_by_user 1 a cada get
        car.save()  # Salvando as alterações do objeto no bd
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['car_brands'] = Brand.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class UpdateCar(UpdateView):
    model = Car
    form_class = RegisterNewCarByUserForm
    template_name = 'update_car.html'
    success_url = reverse_lazy('cars_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['car_brands'] = Brand.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class DeleteCar(DeleteView):
    template_name = 'delete_car.html'
    model = Car
    success_url = reverse_lazy('cars_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['car_brands'] = Brand.objects.all()
        return context


class CarsTopViews(ListView):
    model = Car
    template_name = 'top_views.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['car_brands'] = Brand.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()  # Define queryset como o metodo padrao(car.objects.all())
        queryset = queryset.order_by('-views_by_user')[0:5]  # Ordena car.objects.all do maior para o menor em visualizacoes e pega os 5 primeiros
        return queryset
