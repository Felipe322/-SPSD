from presupuestos.models import Presupuesto, Actividad, Transferencia
from enum import Enum , IntEnum
from django.db import models
from django import forms
from django.forms import ModelForm

class PresupuestoForm(ModelForm):
    class Meta:
        model = Actividad
        fields = ['anio']