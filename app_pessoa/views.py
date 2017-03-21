from django.shortcuts import render

# Create your views here.
from app_pessoa.models import Cargo, Pessoa, Contrato


def index(request):
    lista_de_cargos = Cargo.objects.all()

    return render(request, 'index.html', context={'lista_de_cargos': lista_de_cargos})


def mostrapessoa(request):
    lista_de_pessoas = Pessoa.objects.all()

    return render(request, 'pessoa.html', context={'lista_de_pessoa':lista_de_pessoas})


def mostrarcontrato(request):
    lista_de_contratos = Contrato.objects.all()
    return render(request, 'contrato.html', context={'lista_de_contratos':lista_de_contratos})