"""
Neste arquivo fica o que você quer que o admin do Django gerencie para você
"""
from django.contrib import admin
from app_pessoa.models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    """
    Classe responsável por definir como você quer gerenciar o modelo de dados da Tabela Pessoa
    """
    # list display = lista exibir, como deve ficar a visualização dos dados da tabela
    list_display = ('id', 'nome', 'cpf', 'sexo')

# para que o django entenda que você quer que ele mostre uma classe no admin, basta registrar e referenciar
# as classes que você criou, primeiro o Modelo de dados, e depois a Classe para esse modelo.
admin.site.register(Pessoa, PessoaAdmin)
