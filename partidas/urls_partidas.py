from django.urls import path
from partidas.views import lista_partidas,nueva_partida,eliminar_partida, editar_partida

app_name = 'partidas'

urlpatterns = [
    path('lista/',lista_partidas,name='lista'),
    path('nueva/',nueva_partida,name='nuevo'),
    path('eliminar/<int:clave>',eliminar_partida,name="eliminar"),
    path('editar/<int:clave>',editar_partida,name="editar"),
    
]