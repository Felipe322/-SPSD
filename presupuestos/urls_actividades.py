from django.urls import path
from presupuestos.views import lista_actividades,  \
    nueva_actividad, eliminar_actividad, editar_actividad, traspaso_saldo, \
    nueva_actividad_especifica, historial_traspasos

app_name = 'actividades'

urlpatterns = [
    path('lista/', lista_actividades, name='lista'),
    path('nueva/', nueva_actividad, name='nuevo'),
    path('nueva/<int:id>', nueva_actividad_especifica, name='nueva_especifica'),
    path('eliminar/<int:id>', eliminar_actividad, name="eliminar"),
    path('editar/<int:id>', editar_actividad, name="editar"),
    path('traspaso/', traspaso_saldo, name="traspaso"),
    path('historial-traspasos/', historial_traspasos ,name="historial_traspasos")
]
