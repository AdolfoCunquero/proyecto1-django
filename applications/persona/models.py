from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField(verbose_name="Habilidad", max_length=50)

    def __str__(self) -> str:
        return self.habilidad

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades empleado"


class Empleado(models.Model):

    JOB_CHOICES = [
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Programador'),
        ('4','Otro')
    ]

    first_name = models.CharField(verbose_name="Nombres", max_length=60)
    last_name = models.CharField(verbose_name="Apellidos", max_length=60)
    full_name = models.CharField(verbose_name="Nombre Completo", max_length=120, blank=True)
    job = models.CharField(verbose_name="Trabajo", max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(to=Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="empleado", blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


    class Meta:
        verbose_name = "Empleados"
        verbose_name_plural = "Empleados"
        ordering = ["last_name"]
        unique_together = ["first_name","last_name"]


