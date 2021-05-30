from django.urls import path
from principal.views import principal,seleccionar_anio

app_name = 'principal'

urlpatterns = [
    path('', principal, name='principal'),
    path('seleccionar-anio/',seleccionar_anio,name='seleccionar_anio')
]
