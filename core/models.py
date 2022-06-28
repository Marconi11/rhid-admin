from contextlib import ContextDecorator
import email
from django.db import models

# Create your models here.

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data atualização', auto_now=True)
    ativo = models.BooleanField('Ativo: ', default=True)

    class Meta:
        abstract = True

class Sistema(Base):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Cliente(Base):
    cnpj = models.CharField(max_length=100, unique=True)
    razao_social = models.CharField(max_length=100)
    fantasia = models.CharField(max_length=100)
    sistema = models.ForeignKey(Sistema, on_delete=models.SET_NULL, null=True)
    taxa_adesao = models.DecimalField(max_digits=8,decimal_places=2)
    mensalidade = models.DecimalField(max_digits=8, decimal_places=2)
    contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField()
    quantidade_funcionarios = models.IntegerField()
    vendedor = models.CharField(max_length=100)

    def __str__(self):
        return self.fantasia






class Treinamento(models.Model):
    STATUS = (('P','Pendente'), ('C','Concluido'), ('A', 'Andamento'))
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    sistema = models.ForeignKey(Sistema, on_delete=models.SET_NULL, null=True)
    observacoes = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS, blank=True)


    def __str__(self):
        return str(self.id)
