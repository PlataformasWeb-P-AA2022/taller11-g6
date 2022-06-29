from django import forms
from administrativo.models import *
from django.forms import ModelForm
from dataclasses import fields


class EdicioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo_opciones']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese la direccion por favor'),
            'ciudad': _('Ingrese la ciudad por favor'),
            'tipo_opciones': _('Ingrese el tipo por favor'),
        }

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'Ncuartos',  'edificio']
        labels = {
            'propietario': _('Ingrese nombre de el propietario'),
            'costoDep': _('Ingrese el costo del departamento'),
            'Ncuartos': _('Ingrese el numero de cuartos'),
            'edificio': _('Escoga el edificio'),
        }