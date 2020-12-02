from django.urls import path
from  presupuestos.views import lista_presupuestos, nuevo_presupuesto ,eliminar_presupuesto, editar_presupuesto

app_name = 'presupuestos'

urlpatterns = [
    path('lista/',lista_presupuestos,name='lista'),
    path('nuevo/',nuevo_presupuesto,name='nuevo'),
    path('eliminar/<int:anio>',eliminar_presupuesto,name='eliminar'),
    path('editar/<int:anio>',editar_presupuesto,name="editar"),
]
