from .models import FondoRevolvente
from django.forms import ModelForm
from django import forms


class FondoRevolventeForm(ModelForm):
    class Meta:
        model = FondoRevolvente
        fields = '__all__'