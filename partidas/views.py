from django.shortcuts import render,redirect
from partidas.models import Capitulo, Partida
from partidas.forms import CapituloForm,PartidaForm

###vistas de capitulos
def lista_capitulos(request):
    capitulos = Capitulo.objects.all()
    return render(request, 'lista_capitulos.html',{'capitulos':capitulos})

def nuevo_capitulo(request):
    form = CapituloForm
    if request.method =='POST':
        form = CapituloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capitulos:lista')
    else:
        form = CapituloForm()

    return render(request, 'nuevo_capitulo.html',{'form':form})

def eliminar_capitulo(request,clave):
    partida = Capitulo.objects.get(clave=clave)
    partida.delete()
    return redirect('capitulos:lista')


def editar_capitulo(request,clave):
    capitulo =Capitulo.objects.get(clave=clave)
    if request.method== 'POST':
        form= CapituloForm(request.POST, instance=capitulo)
        if form.is_valid():
            form.save()
            return redirect('capitulos:lista')
    else:
        form= CapituloForm(instance=capitulo)
    return render(request, 'editar_capitulo.html',{'form':form})
        


###vistas de partidas
def lista_partidas(request):
    partidas = Partida.objects.all()
    return render(request, 'lista_partidas.html',{'partidas':partidas})

def nueva_partida(request):
    form = PartidaForm
    if request.method =='POST':
        form = PartidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partidas:lista')
    else:
        form = PartidaForm()
    return render(request,'nueva_partida.html',{'form':form})

def editar_partida(request,clave):
    partida =Partida.objects.get(clave=clave)
    if request.method== 'POST':
        form= PartidaForm(request.POST, instance=partida)
        if form.is_valid():
            form.save()
            return redirect('partidas:lista')
    else:
        form= PartidaForm(instance=partida)
    return render(request, 'editar_partida.html',{'form':form})
        
        
def eliminar_partida(request,clave):
    partida = Partida.objects.get(clave=clave)
    partida.delete()
    return redirect('partidas:lista')

