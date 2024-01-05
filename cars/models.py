from django.db import models


class Brand(models.Model):  # Criacao de um banco de dados para marcas do carro
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name  # Modificando a representação dos objetos para o atributo name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')  # Criando um campo de FK ligando a tabela Brand
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.model  # Configurando para o objeto ser representado pelo seu atributo model
