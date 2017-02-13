from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=250)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    data_nascimento = models.DateField()
