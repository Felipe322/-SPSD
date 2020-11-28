from django.urls import path
from gastos.views import lista_gastos, nuevo_gasto, eliminar_gasto, editar_gasto

app_name = 'gastos'

urlpatterns = [
    path('lista/',lista_gastos,name='lista'),
    path('nueva/',nuevo_gasto,name='nuevo'),
    path('eliminar/<int:id>',eliminar_gasto,name="eliminar"),
    path('editar/<int:id>',editar_gasto,name="editar"),
]