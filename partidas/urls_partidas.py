from django.urls import path
from partidas.views import aniosesion, lista_partidas, nueva_partida, \
    eliminar_partida, editar_partida, nueva_partida_especifica

app_name = 'partidas'

urlpatterns = [
    path('lista/', lista_partidas, name='lista'),
    path('nueva/', nueva_partida, name='nuevo'),
    path('nueva/<int:id>', nueva_partida_especifica, name='nueva_especifica'),
    path('eliminar/<int:clave>', eliminar_partida, name="eliminar"),
    path('editar/<int:clave>', editar_partida, name="editar"),
    path('sesiones/<int:pk>', aniosesion , name='sesiones'),

]
