from presupuestos.models import Presupuesto, Actividad, Transferencia
from django.forms import ModelForm
from enum import Enum , IntEnum
from django.db import models
from django import forms

class PresupuestoForm(ModelForm):
    class Meta:
        model = Presupuesto
        fields = '__all__'


class ActividadForm(ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'


class TransferenciaForm(ModelForm):
    class Meta:
        model = Transferencia
        fields = '__all__'

# class MesFondoRevolvente(IntEnum):
#     Enero = 1
#     Febrero = 2
#     Marzo = 3
#     Abril = 4
#     Mayo = 5
#     Junio = 6
#     Julio = 7
#     Agosto = 8
#     Septiembre = 9
#     Octubre = 10
#     Noviembre = 11
#     Diciembre = 12


class Mes(models.Model):

    class  Nombre(models.IntegerChoices):
        Enero = 1
        Febrero = 2
        Marzo = 3
        Abril = 4
        Mayo = 5
        Junio = 6
        Julio = 7
        Agosto = 8
        Septiembre = 9
        Octubre = 10
        Noviembre = 11
        Diciembre = 12
    mes = models.IntegerField(choices=Nombre.choices)

   
class ActividadForm(ModelForm):   
    class Meta:
        model = Actividad
        fields = ( 'programa', 'componente' , 'actividad' ,'monto',  'descripcion', 'mes', 'partida', 'anio')
        widgets = {
            'programa': forms.NumberInput(attrs={'class': 'form-control'}),
          'componente' : forms.NumberInput(attrs={'class': 'form-control'}),
           'actividad': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
              'descripcion':  forms.TextInput(attrs={'class': 'form-control'}),
               'mes': forms.Select(attrs={'Nombre':'form-control'}),
                'partida': forms.NumberInput(attrs={'class': 'form-control'}),
                 'anio':forms.NumberInput(attrs={'class': 'form-control'}),

        }
    