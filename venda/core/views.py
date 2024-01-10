from django.shortcuts import render, redirect
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

def cadastra_produtos(request):
    return render(request, "cadastraProdutos.html")

def cadastra_produtos_submit(request):
    if request.POST:
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        ficha_tecnica = request.POST.get("ficha_tecnica")
        
        #Realiza o INSERT no banco de dados
        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            ficha_tecnica=ficha_tecnica)
    
    return redirect('/')