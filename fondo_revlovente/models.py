from django.db import models


class FondoRevolvente(models.Model):
    anio = models.CharField('Año', max_length=4, primary_key=True)
    monto = models.DecimalField(
        'Monto', decimal_places=2, max_digits=10, blank=True, null=True)
