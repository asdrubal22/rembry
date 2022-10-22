from django.contrib import admin
from .models import Proyecto,Cita,Estado, Material

# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Cita)
admin.site.register(Estado)
admin.site.register(Material)
