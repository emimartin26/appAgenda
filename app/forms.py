from django import forms
from django.forms import ModelForm
from models import *

class AgendaForm(ModelForm):
    
    class Meta:
        model = Agenda
        exclude = ("user","tarea")
        
class TareaForm(ModelForm):
    
    class Meta:
        model = Tarea
        exclude = ("fecha",) 


class LoginForm(forms.Form):
	username = forms.CharField(widget = forms.TextInput())
	password = forms.CharField(widget = forms.PasswordInput(render_value = False))


