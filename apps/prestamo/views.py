from django.shortcuts import render
from .models import Prestamo

def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamo/lista_prestamos.html', {'prestamos': prestamos})