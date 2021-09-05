from django.db import models

class Departamento(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=50)
    short_name = models.CharField(verbose_name="Nombre Corto", max_length=20, unique=True)
    status = models.BooleanField(verbose_name="Estado", default=True)

    def __str__(self) -> str:
        return str(self.id) + '-'+ self.name + ' - ' + self.short_name


    class Meta:
        verbose_name = "Mi Departamento"
        verbose_name_plural = "Areas de la empresa"
        ordering = ['name']
        unique_together = ["name","short_name"]
        
