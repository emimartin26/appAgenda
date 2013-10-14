from django.shortcuts import render_to_response,get_object_or_404 , render
from django.template.context import RequestContext
from models import *
from forms import AgendaForm, TareaForm , LoginForm, TipoTareaForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import login, authenticate, logout


def home(request):
    template = "index.html"
    return render(request, template,)

@login_required(login_url='/ingresar')
def tareas(request):
    template = "tareas.html"
    agenda = Agenda.objects.get(user = request.user)   #traigo la agenda perteneciente al usuario logueado
    if request.POST:
        form = TipoTareaForm(request.POST)
        if form.is_valid :
            tipo_tarea = request.POST['Tipo_De_Tarea']
            print tipo_tarea
            if tipo_tarea == '-1':
                 tar = agenda.tareas.order_by("fecha")
                 print 'estoy aca'
            else:
                tar_tipo = agenda.tareas.filter(tipo = tipo_tarea)
                tar = tar_tipo.order_by("fecha")
         
    else:        
        form = TipoTareaForm() 
        tar = agenda.tareas.order_by("fecha")  # traigo las tareas de la agenda perteneciente al usuario. 

    ctx = {'agenda':agenda,'tareas':tar, 'form':form, } 
    return render(request,template,ctx,)            
       
   
   


@login_required(login_url='/ingresar')
def detalle_tarea(request, id_tarea):
    tar = get_object_or_404(Tarea,pk = id_tarea) # esto es para que cuando el usario quiera ver una tarea con un id que no exista le devuelva un error 404
    ctx = {'tarea':tar,}
    template = "detalle_tarea.html"
    return render(request,template,ctx,)

@login_required(login_url='/ingresar')
def eliminar_tarea(request, id_tarea):
    tar = get_object_or_404(Tarea, pk = id_tarea)
    tar.delete()
    return HttpResponseRedirect("/tareas")



@login_required(login_url='/ingresar')
def addtarea(request):
    if request.POST:       
        form = TareaForm(request.POST)
        if form.is_valid():
            agenda = Agenda.objects.get(user = request.user)              
            tarea = form.save()  
            tarea.save()
            agenda.tareas.add(tarea)            
            return HttpResponseRedirect("/tareas")
    else:
        form = TareaForm()
    template ="addTarea.html"
    return render(request,template,locals(),)

def ingresar(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect("/logueo")


def logueo(request):
    template ="error.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))


def ingresar(request):
    mensaje = ""
    template = "login.html"
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():                
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']             
                usuario = authenticate(username = username , password= password)                
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect("/")
                else:
                    mensaje = "Usuario y/o password incorrecto"
            else:
               mensaje = "Usuario y/o password incorrecto"     
        form = LoginForm()
        ctx = {'form':form, 'mensaje': mensaje}
        return render_to_response(template,ctx,context_instance= RequestContext(request))

@login_required(login_url = "/login")
def cerrar(request):
    logout(request)
    return HttpResponseRedirect("/")
