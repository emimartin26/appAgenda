from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField

class TipoTarea(models.Model):
    nombre = models.CharField(max_length = 140)
    
    def __unicode__(self):
        return self.nombre
    
class Tarea(models.Model):
    nombre = models.CharField(max_length = 140)
    descripcion = models.TextField(max_length = 500)
    tipo = models.ForeignKey(TipoTarea)
    fecha = models.DateField()
    
    def __unicode__(self):
        return self.nombre
    
    def fecha_rosada(self):
        fec = self.fecha
        return 'http://placehold.it/200x100/E8117F/ffffff/&text=%s' % fec
  
class Agenda(models.Model):
    nombre = models.CharField(max_length = 140)
    user = models.ForeignKey(User)
    tareas = ManyToManyField(Tarea, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
   

        
    







  

    
    


    
    
 
    
