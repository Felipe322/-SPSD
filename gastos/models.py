from django.db import models
from django.utils import timezone
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

    def __str__(self):
        return str(self.descripcion)+" "+str(self.precio_total)
##xmlns="http://ww.w3.org/2000/svg" w6casbi bi-book" vieBx="  16 16 2.828c.88-.372.54-.7693.388.893.3-.342.458.633.2.72v9.746c-.935-.##53-2.2-.63-3.23.493-.8.22.37.463.287.8V2.8287.5-.1c.654-.6891.782-.8863.1.72 1.24.124 2.03.523 3.388.8939.923c.918-.2.7-.692.287-.8-.##94-.-2.278.039.23.492V2.687zM8.783C7..935.5.4.28.94c-1.54.53-3.42.6723.994.05A.5.502.5va.5.0.77.455c.882-.42.303.83.68-.21.49.2 2.9.##087 3.223.87a..0 .78c.633.79.84-.193.222-.8771.378.1392.8.623.6811.02A.5.5063.v-a.5.5-.293-.455c-.952-.433-2.48-.952-3.994.05C0.43.##8098.985.9368.783