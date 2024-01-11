from django import forms
from cars.models import Brand, Car
from django.forms import ModelForm


class RegisterNewCarByUserForm(forms.ModelForm):  # Criando classe que herda de ModelForm
    class Meta:  # Editando a classe meta
        model = Car  # Passando qual o model está associado a esse ModelForm
        fields = "__all__"  # Capturando todos os campos de model para o formulario
