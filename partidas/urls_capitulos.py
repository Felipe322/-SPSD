from django.urls import path
from partidas.views import lista_capitulos, nuevo_capitulo, \
    eliminar_capitulo, editar_capitulo

app_name = 'capitulos'

urlpatterns = [
    path('lista/', lista_capitulos, name='lista'),
    path('nuevo/', nuevo_capitulo, name='nuevo'),
    path('eliminar/<int:clave>', eliminar_capitulo, name="eliminar"),
    path('editar/<int:clave>', editar_capitulo, name="editar"),

]
