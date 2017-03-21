"""
Aqui deve ficar tudo que for referente ao modelo de dados.
Tabelas do banco representadas na forma de classes.
Tabelas abstratas representadas na forma de classes.

Mais informações aqui https://docs.djangoproject.com/pt-br/1.10/topics/db/models/
"""
from django.db import models


class Pessoa(models.Model):
    """
    Classe referente a tabela Pessoa
    """
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1)
    cpf = models.CharField('CPF', max_length=11)
    endereco = models.CharField('Endereço', max_length=250)
    telefone = models.CharField(max_length=20, blank=True,
                                help_text='Informe se o seu celular for da Claro')
    email = models.CharField(max_length=60)
    data_nascimento = models.DateField()

    def __str__(self):
        return 'Pessoa: {} - {}'.format(self.id, self.nome)


class Cargo(models.Model):
    nome_cargo = models.CharField('Nome do Cargo', max_length=30)

    def __str__(self):
        return 'Cargo: {} - {}'.format(self.id, self.nome_cargo)


class Contrato(models.Model):
    id_pessoa = models.ForeignKey(Pessoa, verbose_name='Pessoa')
    id_cargo = models.ForeignKey(Cargo, verbose_name='Cargo')
    data_admissao = models.DateField('Data da Admissão')