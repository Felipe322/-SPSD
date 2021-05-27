from django.db import models
from enum import Enum , IntEnum

class TransactionStatus(Enum):
    INIT = "INITIATED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"

class FondoRevolvente(models.Model):
    anio = models.CharField('Año', max_length=4, primary_key=True)
    monto = models.DecimalField(
        'Monto', decimal_places=2, max_digits=10, blank=True, null=True)

class GastoRevolvente(models.Model):
    PENDIENTE = 'pe'
    PAGADO = 'pa'
    NO_SOLICITADO = 'ns'
    ESTADO_GASTO = (
        (PENDIENTE,'Pendiente'),
        (PAGADO,'Pagado'),
        (NO_SOLICITADO,'No solicitado')
    )

    estatus = models.CharField('estatus',max_length=2, 
        choices = ESTADO_GASTO,
        default = NO_SOLICITADO
    )
    gasto = models.ForeignKey(
        'gastos.Gasto', on_delete=models.CASCADE)
    fondo = models.ForeignKey(
        'fondo_revolvente.FondoRevolvente', on_delete=models.CASCADE)

'''
class MesFondoRevolvente(IntEnum):
    Enero = 1
    Febrero = 2
    Marzo = 3
    Abril = 4
    Mayo = 5
    Junio = 6
    Julio = 7
    Agosto = 8
    Septiembre = 9
    Octubre = 10
    Noviembre = 11
    Diciembre = 12
'''