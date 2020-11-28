from django.urls import path
from presupuestos.views import lista_actividades,nueva_actividad, eliminar_actividad, editar_actividad 

app_name = 'actividades'

urlpatterns = [
    path('lista/',lista_actividades,name='lista'),
    path('nueva/',nueva_actividad,name='nuevo'),
    path('eliminar/<int:id>',eliminar_actividad,name="eliminar"),
     path('editar/<int:id>',editar_actividad,name="editar"),
]