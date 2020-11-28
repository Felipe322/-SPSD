from partidas.models import Partida
from django.db import models
from datetime import datetime
from partidas.models import Partida
from django.utils import timezone

class  Presupuesto(models.Model):
    anio  = models.CharField('Año',max_length=4, primary_key=True)
    fecha= models.DateField('Fecha',default = timezone.now)
     
    def __str__(self):
        return str(self.anio) +" "+str(self.fecha)

class Actividad(models.Model):
    programa = models.CharField('Programa',max_length=2)
    componente= models.CharField('Componente', max_length=2)
    actividad= models.CharField('Actividad', max_length=2)
    monto = models.DecimalField('Monto', decimal_places=2,max_digits=10, blank=True, null=True)
    descripcion= models.CharField('Descripción',max_length=256)
    mes  = models.CharField('Mes', max_length=2)
    partida = models.ForeignKey('partidas.Partida', verbose_name='Partida', on_delete=models.CASCADE)
    anio= models.ForeignKey('presupuestos.Presupuesto',verbose_name='Año', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.programa)+" "+str(self.componente)+" "+str(self.actividad)
    #str(self.monto)+" "+str(self.descripcion)+" "+str(self.mes)+" "+str(self.partida)+" "+str(self.anio)

    
