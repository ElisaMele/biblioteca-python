from django.shortcuts import render
from .models import Socio

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socio/lista_socios.html', {'socios': socios})