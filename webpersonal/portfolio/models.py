from django.db import models

# Create your models here.
class Project(models.Model):
    title =  models.CharField(max_length=200, verbose_name= 'Título') 
    description = models.TextField(verbose_name= 'Descripción')
    #upload_to: Crea un directorio proyects dentro del directorio media 
    image = models.ImageField(verbose_name= 'Imagen', upload_to = 'proyects') 
    #Los siguientes campos no aparecen por defecto en el admin, hay que añadirlos solo lectura en admin.py
    created = models.DateTimeField(auto_now_add= True, verbose_name= 'Fecha de creación') # guarda el momento de la creacion
    updated = models.DateTimeField(auto_now= True, verbose_name= 'Fehca última modificación') #se actualiza cada vez qe se  modifica o se crea una nueva instancia
    url_field = models.URLField(verbose_name= 'Dirección web', null=True, blank= True)

    class Meta: #Para que detecte el nonbre en español del modelo Proyect
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        #campo de ordenacion por defecto la fecha de creacion(se puede ordenar por mas de un campo) 
        ordering = ['-created'] #el '-' hace que ordene en inverso, de fecha mas proxima a mas lejana

    def __str__(self): #Para que nos devuevla nombre de proyecto que ponemos y no uno raro: proyect object(1)
        return self.title