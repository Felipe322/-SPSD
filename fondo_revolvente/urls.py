from django.urls import path
from . import views

app_name = 'fondo'

urlpatterns = [
    path('lista-fondo/', views.FondoRevolventeList.as_view(), name='lista_fondo'),
    path('nuevo-fondo/', views.FondoRevolventeCreate.as_view(), name='nuevo_fondo'),
    #TODO
    # path('nuevo-gasto/', views.nuevo_gasto_revolvente, name='nuevo_gasto'),
]
