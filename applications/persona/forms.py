from django import forms
from applications.persona.models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:

        model = Empleado
        fields = ['first_name',"last_name",'job','departamento','habilidades','avatar']
        custom_attrs = {
                    "class":"form-control"
                }

        widgets = {
            "first_name": forms.TextInput(
                attrs=custom_attrs
            ),
            "last_name": forms.TextInput(
                attrs=custom_attrs
            ),
            "job": forms.Select(
                attrs=custom_attrs
            ),
            "departamento": forms.Select(
                attrs=custom_attrs
            ),
            "habilidades": forms.CheckboxSelectMultiple(
                
            )

        }
