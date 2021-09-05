from django import forms

class NewDepartamentoForm(forms.Form):

    custom_attrs = {
                "class":"form-control"
            }
    widgets = {
            "nombre": forms.TextInput(
                attrs=custom_attrs
            ),
            "apellidos": forms.TextInput(
                attrs=custom_attrs
            ),
            "departamento": forms.TextInput(
                attrs=custom_attrs
            ),
            "short_name": forms.TextInput(
                attrs=custom_attrs
            ),
        }

    nombre = forms.CharField(max_length=50, widget=widgets["nombre"])
    apellidos = forms.CharField(max_length=50, widget=widgets["apellidos"])
    departamento = forms.CharField(max_length=50, widget=widgets["departamento"])
    short_name = forms.CharField(max_length=20, widget=widgets["short_name"])

        
        