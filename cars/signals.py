from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car


@receiver(pre_save, sender=Car)  # Estabelece que essa é uma função receiver que captura o evento pre save do 'remetente' Car
def car_pre_save(sender, instance, **kwargs):
    print(instance)


@receiver(post_save, sender=Car)
def msg_post_save(sender, instance, **kwargs):  # Definimos uma função que será executada quando ocorrer o evento post_save no model Car
    print('--SALVO NO BANCO DE DADOS --- ')


@receiver(pre_delete, sender=Car)
def msg_pre_delete(sender, instance, **kwargs):
    print('----------O OBJETO SERÁ DELETADO DO BD')


@receiver(post_delete, sender=Car)
def msg_post_delete(sender, instance, **kwargs):
    print('-----DELETADO DO BANCO DE DADOS-----')


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
