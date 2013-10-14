from models import Agenda, Tarea
import datetime


def ultimas(request):
	if request.user.is_authenticated():
		agenda = Agenda.objects.get(user = request.user)   #traigo la agenda perteneciente al usuario logueado
		tar = agenda.tareas.order_by("fecha")[:3]  # traigo las tareas de la agenda perteneciente al usuario.
		ctx = {"ultimas":tar,}
	else:
		ctx = {}  
	return ctx

def tareas_hoy(request):
	if request.user.is_authenticated():
		fec_hoy = datetime.date.today()
		agenda = Agenda.objects.get(user = request.user)   #traigo la agenda perteneciente al usuario logueado
		tar = agenda.tareas.filter(fecha = fec_hoy)  
		ctx = {"hoy":tar,}
	else:
		ctx = {}  
	return ctx