"""
URL configuration for venda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exemplo_ola_mundo/', views.exemplo_ola_mundo),
    path('mostra_produtos/', views.mostra_produtos),
    path('cadastra_produtos/', views.cadastra_produtos),
    path('cadastra_produtos/submit', views.cadastra_produtos_submit),
    path('', RedirectView.as_view(url="/mostra_produtos/")), #Definindo a página 'agenda' como Inicial usando RedirectView
]
