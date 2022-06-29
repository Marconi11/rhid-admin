from django.shortcuts import render
from . models import Treinamento

# Create your views here.

def home(request):
    return render(request, 'index.html')


def treinamentos(request):
    treinamentos = Treinamento.objects.all()
    for trei in treinamentos:
        print(trei)
    context = {
        'treinamentos': treinamentos
    }
    return render(request, 'treinamentos.html', context)

def treinamentos_detalhe(request, id):
    treinamentos = Treinamento.objects.get(id=id)
    for trei in treinamentos:
        print(trei)
    context = {
        'treinamentos': treinamentos
    }
    return render(request, 'treinamentos.html', context)


def lista_cliente(request):
    clientes = Cliente.objects.all()
    context = {
        cliente
    }   
    return render(request, 'list-treinamento.html')

def treinamento_detalhe(request):
    return render(request, 'list-treinamento.html')

def cliente_detalhe(request):
    return render(request, 'list-treinamento.html')

def lista_sistema(request):
    return render(request, 'list-treinamento.html')

def sistema_detalhe(request):
    return render(request, 'list-treinamento.html')


def cadastro_clientes(request):
    return render(request, 'cliente.html')