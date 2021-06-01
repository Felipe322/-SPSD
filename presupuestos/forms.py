from re import A

from django.http import request
from partidas.models import Partida
from presupuestos.models import Presupuesto, Actividad, Transferencia
from django.forms import ModelForm
from enum import Enum , IntEnum
from django.db import models
from django import forms
from django.shortcuts import render, HttpResponse 
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


MES_CHOICES= [
(1,'Enero' ),
(2,'Febrero'),
(3,'Marzo'),
(4,'Abril'),
(5,'Mayo' ),
(6,'Junio'),
(7,'Julio'),
(8,'Agosto'),
(9,'Septiembre'),
(10,'Octubre'),
(11,'Noviembre'),
(12,'Diciembre')
]
mes = MES_CHOICES   


MES_NOMBRE_CHOICES= [
('Enero',1 ),
('Febrero',2),
('Marzo', 3),
('Abril', 4),
('Mayo',5 ),
('Junio',6),
('Julio',7),
('Agosto',8),
('Septiembre',9),
('Octubre',10),
('Noviembre',11),
('Diciembre',12)
]
#Ejemplo

#def obtenerAnio(request):
#    if request.session.get['anio']:
#        print(request.session.get['anio'])
#        dic_session= [(request.session.get['anio'],str(request.session.get['anio']))]   
#        
#        return render(request, 'nueva_actividad.html', {'dic_session': dic_session})
        

#ANIO_CHOICES = 
#anio=ANIO_CHOICES

class ActividadForm(ModelForm):   
    mes = forms.ChoiceField(choices=MES_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control'}))
   # anio= forms.ModelChoiceField(required=True, queryset=None)
    
  #  anio = forms.ChoiceField(choices=ANIO_CHOICES, widget=forms.Select(attrs={
   #      'class': 'form-control'}))
    class Meta:
                
        model = Actividad
        fields = ( 'programa', 'componente' , 'actividad' ,'monto', 'mes',  'descripcion', 'partida', 'anio')
        widgets = {
            'programa': forms.NumberInput(attrs={'class': 'form-control'}),
          'componente' : forms.NumberInput(attrs={'class': 'form-control'}),
           'actividad': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
              'descripcion':  forms.TextInput(attrs={'class': 'form-control'}),
                'partida': forms.Select(attrs={'class': 'form-control'}),
               'anio':forms.Select(attrs={'class': 'form-control'}),
        }
        
    #def __init__(self, *args, **kwargs):
    #    self.anio = kwargs.pop('anio')
    #    super(ActividadForm, self).__init__(*args, **kwargs)
    #    self.anio.queryset = Actividad.objects.all().exclude(anio=self.anio)  
          
    # def __str__(self):
    #     return self.get_mes_nombre_display() 
    
    # def __str__(self):
    #     return self.mes_nombre_choices_display() 
    
    