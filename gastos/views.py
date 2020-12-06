from presupuestos.models import Presupuesto
from django.shortcuts import redirect, render
from gastos.forms import GastoForm
from gastos.models import Gasto
<<<<<<< HEAD
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UploadDocumentForm
=======
from django.contrib.auth.decorators import permission_required, login_required

>>>>>>> 2d8475fe4cce62bd24f2a9b679a3d09b4a19d6d9


#Vista gastos
@login_required
def lista_gastos(request):  
    if not request.user.is_authenticated:
        return redirect ('usuarios:login')

    gastos = Gasto.objects.all()
    return render(request, 'lista_gastos.html',{'gastos':gastos})

@login_required
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

@login_required     
def eliminar_gasto(request,id):
    gastos= Gasto.objects.get(id=id)
    gastos.delete()
    return redirect('gastos:lista')

def precio_total(self):
        return self.precio_unitario*self.cantidad

@login_required
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
