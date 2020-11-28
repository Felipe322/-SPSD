from gastos.models import Gasto
from django.forms import ModelForm

class GastoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'

