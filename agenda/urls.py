from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^add/$', 'app.views.add', name= 'add'),
    url(r'^addtarea/$', 'app.views.addtarea', name= 'addtarea'),
    url(r'^ingresar/$', 'app.views.ingresar', name= 'ingresar'),
    url(r'^logueo/$', 'app.views.logueo', name= 'logueo'),
    # url(r'^agenda/', include('agenda.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

     url(r'^admin/', include(admin.site.urls)),
)
