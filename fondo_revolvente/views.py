from django.shortcuts import render
from .models import FondoRevolvente
from django.views.generic import ListView, CreateView
from .forms import FondoRevolventeForm
from django.urls import reverse_lazy

class FondoRevolventeList(ListView):
    paginate_by = 13
    model = FondoRevolvente

class FondoRevolventeCreate(CreateView):
    model = FondoRevolvente
    form_class = FondoRevolventeForm
    success_url = reverse_lazy('principal:principal')

# TODO
# def nuevo_gasto_revolvente(request):
#     form = CategoriaForm()
#     if request.method == 'POST':
#         form = CategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('categoria:lista')
#     context = {'form': form }
#     return render(request, 'nuevo_categoria.html', context)