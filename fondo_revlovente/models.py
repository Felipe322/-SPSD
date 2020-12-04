from django.db import models
from django.db import models
from django.utils import timezone

class FondoRevolvente(models.Model):
    anio =  models.CharField('Año',max_length=4, primary_key=True)
    monto = models.DecimalField('Monto', decimal_places=2,max_digits=10, blank=True, null=True)

class GastoFondo(models.Model):
    fondo_revolvente = models.ForeignKey('fondo_revolvente.FondoRevolvente',verboseName='Año del fondo',on_delete=models.CASCADE)
    