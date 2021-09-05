from django.contrib import admin
from applications.persona.models import Empleado, Habilidades


class EmpleadoAdmin(admin.ModelAdmin):
    model = Empleado
    list_display = ("id","first_name","last_name","departamento","job","full_name2","full_name")

    def full_name2(self, obj):
        return obj.first_name + " - " + obj.last_name

    search_fields = ("first_name",)
    list_filter = ("departamento","job","habilidades")
    filter_horizontal = ("habilidades",)


admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)


# Register your models here.
