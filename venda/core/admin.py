from django.contrib import admin

from core.models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    #Mostra os CAMPOS desejados na rota 'admin/'
    list_display = ('id', 'nome', 'descricao', 'preco', 'ficha_tecnica', 'data_criacao', )

    #Apresenta um filtro interativo pelos CAMPOS definidos
    list_filter = ('nome', 'preco', )

admin.site.register(Produto, ProdutoAdmin)
