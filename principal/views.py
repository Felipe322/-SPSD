from django.shortcuts import render,redirect
from partidas.models import Capitulo, Partida
from gastos.models import Gasto
from presupuestos.models import Actividad
from django.contrib.auth.decorators import login_required
from .forms import PresupuestoForm

# Vista presupuestos


@login_required
def principal(request):
    capitulos = Capitulo.objects.all()
    lista_capitulos = []
    objetos = 1
    for capitulo in capitulos:
        partidas = Partida.objects.filter(capitulo=capitulo.clave)
        lista_partidas = []
        total_capitulo = 0
        total_meses_capitulo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for partida in partidas:
            if request.session['anio']:
                actividades = Actividad.objects.filter(partida=partida.clave).filter(anio=request.session['anio'])
            else:
                actividades = Actividad.objects.filter(partida=partida.clave)
            lista_actividades = {}
            total_partida = 0
            total_meses_partida = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for actividad in actividades:
                if request.session['anio']:
                    gastos = Gasto.objects.filter(id_actividad = actividad.id)
                else:
                    gastos = Gasto.objects.filter(id_actividad = actividad.id).filter(actividad_id__anio = request.session['anio'])
                gasto_actividad = 0
                for gasto in gastos:
                    gasto_actividad+=gasto.precio_total    

                llave = str(actividad.programa)+"-" + \
                    str(actividad.componente) +\
                    "-"+str(actividad.actividad)+"("+str(actividad.anio)+")"
                if llave not in lista_actividades:
                    lista_actividades[str(llave)] = {
                        1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, +
                        8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
                    lista_actividades[str(llave)][int(
                        actividad.mes)] += float(actividad.monto)-float(gasto_actividad) #float
                    total_meses_partida[int(
                        actividad.mes)] += float(actividad.monto)-float(gasto_actividad)
                    total_meses_capitulo[int(
                        actividad.mes)] += float(actividad.monto)-float(gasto_actividad)
                    objetos += 1
                else:
                    lista_actividades[str(llave)][int(
                        actividad.mes)] += float(actividad.monto)-float(gasto_actividad)
                    total_meses_partida[int(
                        actividad.mes)] += float(actividad.monto)-float(gasto_actividad)
                    total_meses_capitulo[int(
                        actividad.mes)] += float(actividad.monto)-float(gasto_actividad)
            lista_actividades2 = []
            for actividad in lista_actividades:
                total_actividad = sum(
                    list(lista_actividades[actividad].values()))
                actividad_estructura = {
                    'id': actividad,
                    'meses': lista_actividades[actividad],
                    'total': total_actividad
                }
                total_partida += total_actividad
                lista_actividades2.append(actividad_estructura)

            partida_estructura = {'id': objetos,
                                  'total': total_partida,
                                  'clave': partida.clave,
                                  'total_meses': total_meses_partida,
                                  'actividades': lista_actividades2
                                  }
            lista_partidas.append(partida_estructura)
            objetos += 1
            total_capitulo += total_partida

        capitulo_estructura = {'id': objetos,
                               'clave': capitulo.clave,
                               'nombre': capitulo.nombre,
                               'partidas': lista_partidas,
                               'total': total_capitulo,
                               'total_meses': total_meses_capitulo,
                               }
        objetos += 1
        lista_capitulos.append(capitulo_estructura)

    data = {'capitulos': lista_capitulos}

    return render(request, 'principal.html', data)

def seleccionar_anio(request):
    form = PresupuestoForm()
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            request.session['anio'] = request.POST.get('anio')
            return redirect('principal:principal')
    else:
        form = PresupuestoForm()
    return render(request,'select_anio.html', {'form': form})