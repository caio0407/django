from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now=True) #Insere a hora atual neste campo
    ficha_tecnica = models.TextField(blank=True, null=True)