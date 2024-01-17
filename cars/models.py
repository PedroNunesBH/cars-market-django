from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone # Importa a funcao timezone
from django.shortcuts import reverse


class Brand(models.Model):  # Criacao de um banco de dados para marcas do carro
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name  # Modificando a representação dos objetos para o atributo name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')  # Criando um campo de FK ligando a tabela Brand
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)  # Definicao de um campo de imagem e aonde elas serão armazenadas
    autor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='car_user', null=True, editable=False)  # Cria um campo de FK associada ao model padrao do django User
    day_time = models.DateTimeField(default=timezone.now, editable=False, null=True)  # Define um campo de data e hora e estabelece como padrao o dia e a hora atual
    views_by_user = models.IntegerField(default=0, editable=False)

    class Meta:
        ordering = ['model']  # Define a ordem que os objetos do model serão recuperados

    def __str__(self):
        return self.model  # Configurando para o objeto ser representado pelo seu atributo model


class CarInventory(models.Model):
    total_cars = models.IntegerField()
    all_cars_value = models.FloatField()
    register_date = models.DateTimeField(auto_now_add=True)  # Registra automaticamente o campo com data e hora atual

    class Meta:
        ordering = ['-register_date']
