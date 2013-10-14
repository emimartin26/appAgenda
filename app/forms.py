#!/usr/bin/env python
#coding: utf8 

from django import forms
from django.forms import ModelForm, Textarea,DateInput
from models import *

#!/usr/bin/python
# -*- encoding: utf-8 -*-

class AgendaForm(ModelForm):
    
    class Meta:
        model = Agenda
        exclude = ("user","tarea")
        
class TareaForm(ModelForm):
   

    class Meta:
        model = Tarea        
        widgets = {
            'fecha': DateInput(attrs={'id': 'datepicker'}),
        }
        placeholder="Type something…"

class LoginForm(forms.Form):
	username = forms.CharField(widget = forms.TextInput(), label='')
	password = forms.CharField(widget = forms.PasswordInput(render_value = False), label = '')
	username.widget.attrs.update({'placeholder' : 'Usuario'})
	password.widget.attrs.update({'placeholder' : 'Contraseña'})

class TipoTareaForm(forms.Form):	
	def cargar():
		tipos = TipoTarea.objects.all()
		lista = [('-1','---------')]
		cont = 0
		for tip in tipos:
			cont= cont + 1
			lista.append(
			(tip.id, tip)
			)	
		return lista


	
	Tipo_De_Tarea = forms.ChoiceField(choices=cargar(), label='')
	Tipo_De_Tarea.widget.attrs.update({'class' : 'input-medium'})

