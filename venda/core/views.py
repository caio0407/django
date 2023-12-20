from django.shortcuts import render
from django.http import HttpResponse

def menu_inicial(request):
    return HttpResponse("""
                        <h1>Olá, Mundo!</h1> <br>
                        <h2>Olá, CAIO!</h2>
                        """)