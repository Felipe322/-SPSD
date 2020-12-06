from django.db import models
from django.utils import timezone
from presupuestos.models import Actividad
from django.core.validators import MaxValueValidator, MinValueValidator


class Gasto(models.Model):
    descripcion = models.CharField('Descripción', max_length=256)
    proveedor = models.CharField('Proveedor', max_length=200)
    precio_unitario = models.FloatField('Precio Unitario', max_length=9)
    cantidad = models.PositiveIntegerField(
        'Cantidad', validators=[MaxValueValidator(100000),
                                MinValueValidator(1)])
    precio_total = models.FloatField(
        'Total', editable=False, validators=[MaxValueValidator(1000000),
                                             MinValueValidator(0)])
    fecha = models.DateField('Fecha', default=timezone.now)
    factura = models.FileField(
        'Factura', upload_to="facturas", max_length=254, blank=True,
        null=True)
    id_actividad = models.ForeignKey(
        'presupuestos.Actividad', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.precio_total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

# default=get_next_increment, editable=False

    def __str__(self):
        return str(self.descripcion)+" "+str(self.precio_total)
