
from presupuestos.models import Presupuesto
from django.shortcuts import redirect, render
from gastos.forms import GastoForm
from gastos.models import Gasto



#Vista gastos

def lista_gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'lista_gastos.html',{'gastos':gastos})

def nuevo_gasto(request):
    form =GastoForm
    if request.method== 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gastos:lista')
    else:
        form = GastoForm()
    return render(request,'nuevo_gasto.html',{'form':form})
        
def eliminar_gasto(request,id):
    gastos= Gasto.objects.get(id=id)
    gastos.delete()
    return redirect('gastos:lista')

def precio_total(self):
        return self.precio_unitario*self.cantidad

def editar_gasto(request,id):
    gasto =Gasto.objects.get(id=id)
    if request.method== 'POST':
        form= GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('gastos:lista')
    else:
        form= GastoForm(instance=gasto)
    return render(request, 'editar_gasto.html',{'form':form})
        