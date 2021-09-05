from django.urls import path
from applications.persona.views import (ListAllEmpleados,
                                        ListByAreaEmpleados,
                                        ListByKwordEmpleados,
                                        ListHabilidadesEmpleado,
                                        DetailViewEmpleado,
                                        CreateViewEmpleado,
                                        SuccessView,
                                        UpdateViewEmpleado,
                                        DeleteViewEmpleado,
                                        HomeView,
                                        ListAdminEmpleados
                                        )

app_name = "persona_app"

urlpatterns = [
    path('list-all/',  ListAllEmpleados.as_view(), name="listar_empleados"),
    path('list-by-area/<str:departamento>/',  ListByAreaEmpleados.as_view(), name="empleados_area"),
    path('list-by-kword/',  ListByKwordEmpleados.as_view()),
    path('habilidades/<int:id>/',  ListHabilidadesEmpleado.as_view(), name="habilidades_empleado"),
    path('detail/<int:pk>/',  DetailViewEmpleado.as_view(), name="detalle_empleado"),
    path('create/',  CreateViewEmpleado.as_view(), name="empleado_add"),
    path('success/',  SuccessView.as_view()),
    path('update/<int:pk>',  UpdateViewEmpleado.as_view(), name ="update_empleado"),
    path('delete/<int:pk>',  DeleteViewEmpleado.as_view(), name="delete_empleado"),
    path('',  HomeView.as_view(), name="home"),
    path('list-admin',  ListAdminEmpleados.as_view(), name="empleados_admin"),
]