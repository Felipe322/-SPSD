from django.shortcuts import render
from partidas.models import Capitulo, Partida
from presupuestos.models import Actividad , Presupuesto
from gastos.models import Gasto

#Vista presupuestos
def principal(request):
    capitulos = Capitulo.objects.all()
    lista_capitulos = []
    objetos = 1

    for capitulo in capitulos:
        partidas = Partida.objects.filter(capitulo=capitulo.clave)
        lista_partidas = []
        total_capitulo = 0
        for partida in partidas:
            actividades = Actividad.objects.filter(partida=partida.clave)
            lista_actividades = []
            total_partida = 0
            for actividad in actividades:
                #
                #
                actividad_estructura = {'id':objetos,
                                        'programa': actividad.programa,
                                        'componente': actividad.componente,
                                        'actividad':actividad.actividad,    
                                        'monto':actividad.monto,
                                        'descripcion': actividad.descripcion,
                                        'mes':actividad.mes,
                                        'partida':actividad.partida,
                                        'anio':actividad.anio
                                     }
                total_partida+=actividad.monto
                lista_actividades.append(actividad_estructura)
                objetos+=1
            partida_estructura = {'id':objetos,
                                'total': total_partida,
                                'clave':partida.clave,
                                'nombre':partida.nombre,
                                'descripcion':partida.descripcion,
                                'actividades':lista_actividades
                                }
            lista_partidas.append(partida_estructura)
            objetos+=1
            total_capitulo+=total_partida

        capitulo_estructura = {'id':objetos,
                                'clave':capitulo.clave,
                                'nombre':capitulo.nombre,
                                'partidas': lista_partidas,
                                'total':total_capitulo
                                }
        objetos+=1
        lista_capitulos.append(capitulo_estructura)

    data = {'capitulos': lista_capitulos}
    return render(request, 'principal.html',data)
