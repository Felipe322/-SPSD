from .models import FondoRevolvente
from django.forms import ModelForm
from django import forms


class FondoRevolventeForm(ModelForm):
    class Meta:
        model = FondoRevolvente
        fields = '__all__'
        
        
#
#class FondoRevolventeForm(ModelForm):   
#    class Meta:
#        model = FondoRevolvente
#        fields = ( 'anio', 'monto')
#        widgets = {
#                 'anio':forms.Select(attrs={'class': 'form-control'}),
#                'monto': forms.NumberInput(attrs={'class': 'form-control'}),
#
#        }