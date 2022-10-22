from django.db import models
from proyecto.models import Proyecto


# Create your models here.

class Empleado(models.Model):
    identificacion = models.CharField(max_length=100, blank=False)
    primer_nombre = models.CharField(max_length=100, blank=False)
    segundo_nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100,blank=False)
    segundo_apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(blank=False, null=True)
    celular = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.primer_nombre


class Asignacion_Empleado(models.Model):
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name="empleados")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyecto")

    def __str__(self):
        return str(self.proyecto)


