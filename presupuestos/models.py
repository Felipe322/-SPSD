from django.db import models
from django.utils import timezone
from django.core.validators import  MaxValueValidator, MinValueValidator, MaxLengthValidator, RegexValidator, validate_slug


class Presupuesto(models.Model):
    anio = models.CharField('Año', max_length=4, primary_key=True,validators=[RegexValidator( regex='[0-9]{4,4}',message='Ingrese un año válido')])
    fecha = models.DateField('Fecha', default=timezone.now)

    def __str__(self):
        return str(self.anio)



class Actividad(models.Model):
    programa = models.CharField('Programa', max_length=2 ,)
    componente = models.CharField('Componente', max_length=2)
    actividad = models.CharField('Actividad', max_length=2)
    monto = models.DecimalField(
        'Monto', decimal_places=2, max_digits=10, blank=True, null=True,
        validators=[MaxValueValidator(
        9999999.99), MinValueValidator(0,"El monto no puede ser menor a 0")])
    descripcion = models.CharField('Descripción', max_length=2300)
    mes = models.CharField('Mes', max_length=2, 
                           validators=[RegexValidator(regex='[1-9]|1[0-2]',message='Ingrese un mes válido')])
    partida = models.ForeignKey(
        'partidas.Partida', verbose_name='Partida', on_delete=models.CASCADE)
    anio = models.ForeignKey('presupuestos.Presupuesto',
                             verbose_name='Año', on_delete=models.CASCADE,
                             )

    def __str__(self):
        return str(self.programa)+" "+str(self.componente)+" " \
            + str(self.actividad)+"-"+str(self.descripcion) + \
            "Saldo: "+str(self.monto)+"$ partida "+str(self.partida)
    # str(self.monto)+" "+str(self.descripcion)+" "+str(self.mes)+"
    # "+str(self.partida)+" "+str(self.anio)


class Transferencia(models.Model):
    actividad1 = models.ForeignKey('presupuestos.Actividad',
                                   related_name='actividad1',
                                   verbose_name='Actividad Remitente',
                                   on_delete=models.CASCADE)
    actividad2 = models.ForeignKey('presupuestos.Actividad',
                                   related_name='actividad2',
                                   verbose_name='Actividad Destino',
                                   on_delete=models.CASCADE)
    monto = models.DecimalField(
        'Monto', decimal_places=2, max_digits=10, blank=False, null=False)
