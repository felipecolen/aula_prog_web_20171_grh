"""
Aqui deve ficar tudo que for referente ao modelo de dados.
Tabelas do banco representadas na forma de classes.
Tabelas abstratas representadas na forma de classes.
"""
from django.db import models


class Pessoa(models.Model):
    """
    Classe referente a tabela Pessoa
    """
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    data_nascimento = models.DateField()
