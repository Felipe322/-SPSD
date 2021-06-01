from django.shortcuts import redirect, render
from gastos.forms import GastoForm
from gastos.models import Gasto
from presupuestos.models import Actividad
from django.contrib.auth.decorators import login_required
from django.db.models import F


# Vista gastos
@login_required
def lista_gastos(request):
    if request.session.get('anio'):
        gastos = Gasto.objects.filter(id_actividad__anio =request.session['anio'])
        
    else:
        gastos = Gasto.objects.all()
    return render(request, 'lista_gastos.html', {'gastos': gastos})


@login_required
def nuevo_gasto(request):
    form = GastoForm
    if request.method == 'POST':
        form = GastoForm(request.POST)
        id_actividad = request.POST['id_actividad']
        precio_unitario = request.POST['precio_unitario']
        cantidad = request.POST['cantidad']
        total_gasto = float(precio_unitario) * float(cantidad)
        
        
        #return render(request, 'nueva_actividad.html', {'dic_session': dic_session})
        ###
        ##
        if form.is_valid():
            if gasto_valido(form):
                form.save()
                ##Código restar a actividad
                #actividad = Actividad.objects.filter(id=id_actividad).update(
                #    monto=F('monto')-total_gasto)
                return redirect('gastos:lista')
            else:
                error = 'Error, favor de proporcionar un gasto válido.'
                return redirect(error)
    else:
        form = GastoForm()
    return render(request, 'nuevo_gasto.html', {'form': form})


@login_required
def eliminar_gasto(request, id):
    gastos = Gasto.objects.get(id=id)
    gastos.delete()
    return redirect('gastos:lista')


def precio_total(self):
    return self.precio_unitario*self.cantidad


@login_required
def editar_gasto(request, id):
    gasto = Gasto.objects.get(id=id)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('gastos:lista')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'editar_gasto.html', {'form': form})


def gasto_valido(form):
    actividad = Actividad.objects.get(id=form.cleaned_data['id_actividad'].id)
    disponible = actividad.monto
    cantidad = form.cleaned_data['cantidad']
    precio = form.cleaned_data['precio_unitario']
    if (cantidad * precio) < disponible:
        return True
    else:
        return False