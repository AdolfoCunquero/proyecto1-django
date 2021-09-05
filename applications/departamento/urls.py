from django.urls import path
from applications.departamento.views import DepartamentoFormView,DepartamentoListView

app_name = "departamento"

urlpatterns = [
    path('create/', DepartamentoFormView.as_view(), name="create_departamento"),
    path('list/', DepartamentoListView.as_view(), name="list_departamento"),
]