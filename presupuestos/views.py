from presupuestos.forms import ActividadForm, PresupuestoForm, \
    TransferenciaForm 
from django.shortcuts import redirect, render
from presupuestos.models import Presupuesto, Actividad, Transferencia
from partidas.models import Partida
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import F
from django import template

# Create your views here.

# Vista presupuestos
@login_required
def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'lista_presupuestos.html', {'presupuestos':
                                                       presupuestos})


@login_required
@permission_required('presupuestos.add_presupuesto', raise_exception=True)
def nuevo_presupuesto(request):
    form = PresupuestoForm
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presupuestos:lista')
    else:
        form = PresupuestoForm()
    return render(request, 'nuevo_presupuesto.html', {'form': form})


@login_required
@permission_required('presupuestos.delete_presupuesto', raise_exception=True)
def eliminar_presupuesto(request, anio):
    presupuesto = Presupuesto.objects.get(anio=anio)
    presupuesto.delete()
    return redirect('presupuestos:lista')


@login_required
@permission_required('presupuestos.change_presupuesto', raise_exception=True)
def editar_presupuesto(request, anio):
    presupuesto = Presupuesto.objects.get(anio=anio)
    if request.method == 'POST':
        form = PresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():
            form.save()
            return redirect('presupuestos:lista')
    else:
        form = PresupuestoForm(instance=presupuesto)
    return render(request, 'editar_presupuestos.html', {'form': form})


# Vista actividades

@login_required
def lista_actividades(request):
    actividades = None
    if request.session.get('anio'):
        actividades = Actividad.objects.filter(anio=request.session['anio'])
    else:
        actividades = Actividad.objects.all()   

    return render(request, 'lista_actividades.html',
                  {'actividades': actividades})

@login_required
@permission_required('actividades.add_actividad', raise_exception=True)
def nueva_actividad(request):
    form = ActividadForm
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actividades:lista')
    else:
        form = ActividadForm()
    return render(request, 'nueva_actividad.html', {'form': form }) #

@login_required
@permission_required('actividades.add_actividad', raise_exception=True)
def nueva_actividad_especifica(request, id):
    partida = Partida.objects.get(clave=id)
    context = {}
    initial_dict = {
        "partida" : partida.clave,
    }

    form = ActividadForm(initial = initial_dict)
    context['form']= form

    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal:principal')
    else:
        form = ActividadForm()
    return render(request, 'nueva_actividad.html', context)

@login_required
@permission_required('actividades.delete_actividad', raise_exception=True)
def eliminar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)
    actividad.delete()
    return redirect('actividades:lista')


@login_required
@permission_required('actividades.change_actividad', raise_exception=True)
def editar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividades:lista')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'editar_actividad.html', {'form': form})


@login_required
@permission_required('actividades.add_traspaso', raise_exception=True)
def traspaso_saldo(request):
    form = TransferenciaForm()
    if request.method == 'POST':
        form = TransferenciaForm(request.POST)
        id_actividad1 = request.POST['actividad1']
        id_actividad2 = request.POST['actividad2']
        monto_traspaso = request.POST['monto']
        saldo_disponible = Actividad.objects.values_list(
            'monto').get(id=id_actividad1)[0]
        if float(monto_traspaso) > float(saldo_disponible):
            print("Error No se puede transpasar")
        else:
            if form.is_valid():
                Actividad.objects.filter(id=id_actividad1).update(
                    monto=F('monto')-monto_traspaso)
                Actividad.objects.filter(id=id_actividad2).update(
                    monto=F('monto')+monto_traspaso)
                form.save()
    return render(request, 'traspaso_saldo.html', {'form': form})


def traspaso_saldo_validar(form):
    actividad = Actividad.objects.get(id=form.cleaned_data['id_actividad'].id)
    monto = form.cleaned_data['monto']
    if (actividad - monto ) > 0: ## Restar el gasto ????
        return True
    else:
        return False

# Vista presupuestos
@login_required
def historial_traspasos(request):
    traspasos = Transferencia.objects.all()
    return render(request, 'historial_traspasos.html', {'traspasos':
                                                       traspasos})
