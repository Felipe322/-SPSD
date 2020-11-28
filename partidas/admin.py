from django.contrib import admin
from partidas.models import Capitulo,Partida
from presupuestos.models import Presupuesto, Actividad
from gastos.models import Gasto

admin.site.register(Capitulo)
admin.site.register(Partida)
admin.site.register(Presupuesto)
admin.site.register(Actividad)
admin.site.register(Gasto)

