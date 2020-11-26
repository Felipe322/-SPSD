from presupuestos.models import Presupuesto,Actividad
from django.forms import ModelForm

class PresupuestoForm(ModelForm):
    class Meta:
        model = Presupuesto
        fields = '__all__'

class ActividadForm(ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'