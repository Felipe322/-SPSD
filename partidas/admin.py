from django.contrib import admin
from partidas.models import Capitulo, Partida
from presupuestos.models import Presupuesto, Actividad, Transferencia
from fondo_revolvente.models import FondoRevolvente,GastoRevolvente
from gastos.models import Gasto

admin.site.register(Capitulo)
admin.site.register(Partida)
admin.site.register(Presupuesto)
admin.site.register(Actividad)
admin.site.register(Gasto)
admin.site.register(Transferencia)
admin.site.register(FondoRevolvente)
admin.site.register(GastoRevolvente)
