from django.urls import path
from .views import PruebaView, PruebaListView, ListarPrueba, PruebaCreateView

urlpatterns = [
    path('', PruebaView.as_view()),
    path('list/', PruebaListView.as_view()),
    path('lista-prueba/', ListarPrueba.as_view()),
    path('add-prueba/', PruebaCreateView.as_view()),
]