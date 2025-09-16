from django.shortcuts import render
from .models import Autor

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'autor/lista_autores.html', {'autores': autores})