from gastos.models import Gasto
from django.forms import ModelForm
from django import forms
class GastoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'

class UploadDocumentForm(forms.Form):
    file = forms.FileField()
    image = forms.ImageField()
