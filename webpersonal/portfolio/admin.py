from django.contrib import admin
from .models import Project

# Register your models here.

#Clase para extender las funcionalidades del panel de admin
class ProyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #redefinimos para que muestre los campos de fechas de models.py

admin.site.register(Project , ProyectAdmin) #registramos un nuevo modelo. Le pasamos la configuracion extenduda para las fechas.


