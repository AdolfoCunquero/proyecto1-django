from django.db import models
from django.db.models import query
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from applications.home.forms import HomeForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = "home/list.html"
    context_object_name = "lista_numeros"

    queryset = [
        '0','1','10','20','30'
    ]


class ListarPrueba(ListView):
    template_name = "home/list_prueba.html"
    model = Prueba
    context_object_name = "data"

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    success_url = "/"
    form_class = HomeForm
    