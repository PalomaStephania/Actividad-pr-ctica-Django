from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Vista basada en clase para mostrar una lista
class IndexView(TemplateView):
    template_name = 'home.html'

# Vista para probar una lista estática
class PruebaLista(ListView):
    template_name = 'lista.html'
    queryset = ['A', 'B', 'C', 'D']
    context_object_name = 'lista_prueba'

class ArraysView(TemplateView):
    template_name = "arrays.html"
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis"]
    apellidos = ["Pérez", "González", "Ramírez", "López", "Martínez"]
    edades = [25, 30, 22, 28, 35]
    context_object_name = 'Arrays'