from django.contrib import admin
from models import *
import datetime

from actions import export_as_csv
    
class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','tipo','fecha_rosadita','dias',)
    list_filter =('nombre','tipo', 'fecha')
    search_fields = ('nombre',)
    list_editable = ('descripcion','tipo',)
    list_display_links = ('nombre',)
    raw_id_fields = ('tipo',)
    actions = [export_as_csv]
    
    def fecha_rosadita(self, obj):
        url = obj.fecha_rosada()
        tag = '<img src="%s">' % url
        return tag

    def dias(self, obj):
        dias = obj.dias()
        tag = '%s' % dias
        return tag
        
    
    
    fecha_rosadita.allow_tags = True



    
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nombre','user')
    filter_horizontal = ('tareas',)
    actions = [export_as_csv]
   
    

   








admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(TipoTarea)


