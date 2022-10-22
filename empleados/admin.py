from django.contrib import admin
from .models import Empleado, Asignacion_Empleado

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Asignacion_Empleado)
