from typing import List
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from applications.persona.models import Empleado
from django.urls import reverse_lazy
from applications.persona.forms import EmpleadoForm

class HomeView(TemplateView):
    template_name ="home.html"

class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    #model = Empleado
    paginate_by = 5
    context_object_name = "empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        return Empleado.objects.filter(full_name__icontains = palabra_clave)


class ListAdminEmpleados(ListView):
    template_name = "persona/list_empleados_admin.html"
    model = Empleado
    paginate_by = 5
    context_object_name = "empleados"


class ListByAreaEmpleados(ListView):
    template_name ="persona/list_by_area.html"
    context_object_name = "empleados"

    def get_queryset(self):
        departamento = self.kwargs["departamento"]
        lista = Empleado.objects.filter(departamento__short_name = departamento)
        return lista


class ListByKwordEmpleados(ListView):
    template_name = "persona/list_by_kword.html"
    context_object_name = "empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",)
        return Empleado.objects.filter(first_name = palabra_clave)
        

class ListHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = "habilidades"
    
    def get_queryset(self):
        empleado_id = self.kwargs["id"]
        empleado = Empleado.objects.get(id=empleado_id)
        return empleado.habilidades.all()


class DetailViewEmpleado(DetailView):
    model = Empleado
    template_name = "persona/detail.html"
    context_object_name = "empleado"

    def get_context_data(self, **kwargs):
        context = super(DetailViewEmpleado, self).get_context_data(**kwargs)
        context['titulo'] = "Empleado del mes"
        return context

class SuccessView(TemplateView):
    template_name = "persona/success.html"



class CreateViewEmpleado(CreateView):
    template_name = "persona/create.html"
    model = Empleado
    form_class = EmpleadoForm
    #fields = ["first_name","last_name","departamento","job","habilidades"]
    success_url = reverse_lazy("persona_app:empleados_admin")


    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(CreateViewEmpleado, self).form_valid(form)


class UpdateViewEmpleado(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("persona_app:empleados_admin")
    #fields = ["first_name","last_name","departamento","job","habilidades"]

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(UpdateViewEmpleado, self).form_valid(form)


class DeleteViewEmpleado(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy("persona_app:empleados_admin")
