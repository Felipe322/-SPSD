from partidas.models import Capitulo,Partida
from django.forms import ModelForm

class CapituloForm(ModelForm):
    class Meta:
        model = Capitulo
        fields = '__all__'

class PartidaForm(ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'