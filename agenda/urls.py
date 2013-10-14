from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^ingresar/$', 'app.views.ingresar', name='ingresar'),
    url(r'^cerrar/$', 'app.views.cerrar', name='cerrar'),
    url(r'^tareas/$', 'app.views.tareas', name = 'tareas'),
    url(r'^addtarea/$', 'app.views.addtarea', name= 'addtarea'),
    url(r'^ingresar/$', 'app.views.ingresar', name= 'ingresar'),
    url(r'^logueo/$', 'app.views.logueo', name= 'logueo'),
    url(r'^detalle/(\d+)$','app.views.detalle_tarea', name='detalle'),
    url(r'^eliminar/(\d+)$' , 'app.views.eliminar_tarea', name='eliminar_tarea'),
   
    # url(r'^agenda/', include('agenda.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

     url(r'^admin/', include(admin.site.urls)),
)
