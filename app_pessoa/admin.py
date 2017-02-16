from django.contrib import admin

# Register your models here.
from app_pessoa.models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'sexo')

admin.site.register(Pessoa, PessoaAdmin)