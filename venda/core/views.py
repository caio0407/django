from django.shortcuts import render
from django.http import HttpResponse
from core.models import Produto

def exemplo_ola_mundo(request):
    return HttpResponse("""
                        <h1>Olá, Mundo!</h1> <br>
                        <h2>Olá, CAIO!</h2>
                        """)

def mostra_produtos(request):
    produtos = Produto.objects.all() #Obtem TODOS os dados do BD
    produtos = produtos.order_by('preco') #Ordena eventos por Preco
    dados = {'produtos': produtos}
    return render(request, "produtos.html", dados)