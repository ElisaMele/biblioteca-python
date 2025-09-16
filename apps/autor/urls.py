from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_autores, name='lista_autores'),
]
