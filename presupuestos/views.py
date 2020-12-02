from partidas.forms import PartidaForm
from presupuestos.forms import ActividadForm, PresupuestoForm,TransferenciaForm
from django.shortcuts import redirect, render
from presupuestos.models import Presupuesto, Actividad
from django.db.models import F


# Create your views here.

#Vista presupuestos
def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'lista_presupuestos.html',{'presupuestos':presupuestos})

def nuevo_presupuesto(request):
    form =PresupuestoForm
    if request.method =='POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presupuestos:lista')
    else:
        form = PresupuestoForm()
    return render(request, 'nuevo_presupuesto.html',{'form':form})


def eliminar_presupuesto(request,anio):
    presupuesto = Presupuesto.objects.get(anio=anio)
    presupuesto.delete()
    return redirect('presupuestos:lista') 


def editar_presupuesto(request,anio):
    presupuesto =Presupuesto.objects.get(anio=anio)
    if request.method== 'POST':
        form= PresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():
            form.save()
            return redirect('presupuestos:lista')
    else:
        form= PresupuestoForm(instance=presupuesto)
    return render(request, 'editar_presupuesto.html',{'form':form})
        

#Vista actividades


def lista_actividades(request):
    actividades= Actividad.objects.all()
    return render(request, 'lista_actividades.html',{'actividades':actividades})

def nueva_actividad(request):
    form = ActividadForm
    if request.method =='POST':
        form= ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actividades:lista')
    else:
        form = ActividadForm()
    return render(request,'nueva_actividad.html',{'form':form})

def eliminar_actividad(request,id):
    actividad= Actividad.objects.get(id=id)
    actividad.delete()
    return redirect('actividades:lista')

def editar_actividad(request,id):
    actividad = Actividad.objects.get(id=id)
    if request.method== 'POST':
        form= ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividades:lista')
    else:
        form= ActividadForm(instance=actividad)
    return render(request, 'editar_actividad.html',{'form':form})
        
def traspaso_saldo(request,id):
    form = TransferenciaForm()
    if request.method == 'POST':
        form = TransferenciaForm(request.POST)
        id_actividad1 = request.POST['actividad1']
        id_actividad2 = request.POST['actividad2']
        monto_traspaso = request.POST['monto']
        saldo_disponible= Actividad.objects.values_list('monto').get(id=id_actividad1)[0]
        if float(monto_traspaso) > float(saldo_disponible):
            print("Error No se puede transpasar")
        else:
            if form.is_valid():
                Actividad.objects.filter(id=id_actividad1).update(monto=F('monto')-monto_traspaso)
                Actividad.objects.filter(id=id_actividad2).update(monto=F('monto')+monto_traspaso)
                form.save()
    return render(request,'traspaso_saldo.html',{'form':form})