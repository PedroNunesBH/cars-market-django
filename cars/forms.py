from django import forms
from cars.models import Car
from django.forms import ModelForm


class RegisterNewCarByUserForm(forms.ModelForm):  # Criando classe que herda de ModelForm
    class Meta:  # Editando a classe meta
        model = Car  # Passando qual o model está associado a esse ModelForm
        fields = "__all__"  # Capturando todos os campos de model para o formulario

    def clean_value(self):  # Criacao de um metodo de validacao do campo value do model associado
        value = self.cleaned_data.get('value')  # Capturando o valor do campo value
        if value < 20000:  # Verifica se é menor que 20000
            self.add_error('value', "O valor mínimo é R$20000")  # Emite um erro recebendo como argumento o campo e a msg de erro
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')  # Capturando o valor do campo factory_year
        if factory_year < 1980:
            self.add_error('factory_year', "O ano de fabricação mínimo é 1980.")
        return factory_year

    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        if len(plate) < 8:
            self.add_error('plate', "Insira uma placa válida.")

    def clean_model_year(self):  # Criando um metodo de validacao do formulario (indicado pelo clean_)
        model_year = self.cleaned_data.get('model_year')  # Capturando o valor de model_year
        if model_year > 2025:
            self.add_error('model_year', "Insira um ano de modelo correto.")  # Adicionando a mensagem de erro
