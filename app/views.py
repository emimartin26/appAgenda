from django.shortcuts import render_to_response,get_object_or_404
from django.template.context import RequestContext
from models import *
from forms import AgendaForm, TareaForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist



def home(request):
    template = "index.html" 
    return render_to_response(template)

def tareas(request):
    template = "tareas.html"
    try:
        agenda = Agenda.objects.get(user = request.user)   #traigo la agenda perteneciente al usuario logueado
        tar = agenda.tareas.all()  # traigo las tareas de la agenda perteneciente al usuario.
     
        ctx = {'agenda':agenda,'tareas':tar, }  
        return render_to_response(template,ctx,context_instance=RequestContext(request))
    except ObjectDoesNotExist, e:
        print 'erorrrr no hay agendas'
   
    return render_to_response(template)


def detalle_tarea(request, id_tarea):
    tar = get_object_or_404(Tarea,pk = id_tarea) # esto es para que cuando el usario quiera ver una tarea con un id que no exista le devuelva un error 404
    ctx = {'tarea':tar,}
    template = "detalle_tarea.html"
    return render_to_response(template,ctx,context_instance=RequestContext(request))

def eliminar_tarea(request, id_tarea):
    tar = get_object_or_404(Tarea, pk = id_tarea)
    tar.delete()
    return HttpResponseRedirect("/tareas")


@login_required(login_url='/ingresar')
def add(request):
    if request.POST:       
        form = AgendaForm(request.POST)
        if form.is_valid():
            agenda = form.save(commit = False)
            agenda.user = request.user
            agenda.save()
            return HttpResponseRedirect("/")
    else:
        form = AgendaForm()
    template ="formulario.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))


@login_required(login_url='/ingresar')
def addtarea(request):
    if request.POST:       
        form = TareaForm(request.POST)
        if form.is_valid():
            #aca tendria que buscar la agenda del usuario logueado y agregarle la nueva tarea.
            agenda = Agenda.objects.get(user = request.user) 
            tarea = form.save(commit = False) 
            tarea.fecha = request.POST["fecha"]           
            tarea.save()
            agenda.tareas.add(tarea)            
            return HttpResponseRedirect("/tareas")
    else:
        form = TareaForm()
    template ="addTarea.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

def ingresar(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect("/logueo")


def logueo(request):
    template ="error.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))
    