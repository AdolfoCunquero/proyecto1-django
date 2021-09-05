from django.shortcuts import render
from applications.departamento.forms import NewDepartamentoForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from applications.departamento.models import Departamento
from applications.persona.models import Empleado

class DepartamentoListView(ListView):
    template_name = "departamento/list.html"
    model = Departamento
    context_object_name = "departamentos"

class DepartamentoFormView(FormView):
    template_name = "departamento/create.html"
    form_class = NewDepartamentoForm
    success_url = "/departamento/list"

    def form_valid(self, form):
        nombre = form.cleaned_data["nombre"]
        apellidos = form.cleaned_data["apellidos"]
        departamento = Departamento(
            name = form.cleaned_data["departamento"],
            short_name = form.cleaned_data["short_name"]
        )

        departamento.save()

        Empleado.objects.create(first_name = nombre, last_name=apellidos, job='1', departamento=departamento)
        return super(DepartamentoFormView, self).form_valid(form)


