from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum


@receiver(pre_save, sender=Car)  # Estabelece que essa é uma função receiver que captura o evento pre save do 'remetente' Car
def car_pre_save(sender, instance, **kwargs):
    print(instance)


@receiver(post_save, sender=Car)
def email_novo_carro(sender, instance, **kwargs):
    print(f'Acaba de ser cadastrado um novo carro no sistema!'
                                f'Modelo : {instance}.'
                                f'Marca : {instance.brand}.'
                                f'Placa : {instance.plate}.'
                                f'Autor: {instance.autor}.'
                                f'Data e Hora : {instance.day_time}')


@receiver(post_delete, sender=Car)
def notification_delete(sender, instance, **kwargs):
    print(f'-----OBJETO { instance } deletado----------')


def car_inventory_update():
    total_cars = Car.objects.all().count()  # Faz uma query atarves do ORM que retorna a quantidade de carros no bd
    total_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']  # Cria o campo total_value que tem o valor da soma do campo value de carro e retorna em um dict onde acessamos atraves da chave
    CarInventory.objects.create(total_cars=total_cars, all_cars_values=total_value)  # Cria um registro no modelo recebendo como parametro os campos e valores


@receiver(post_save, sender=Car)
def update_inventory_add_car(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def update_inventory_delete_car(sender, instance, **kwargs):
    car_inventory_update()
