from presupuestos.models import Presupuesto,Actividad,Transferencia
from django.forms import ModelForm

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