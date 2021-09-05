from django.db import models

class Prueba(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=150)
    cantidad = models.IntegerField()


    def __str__(self):
        return self.titulo