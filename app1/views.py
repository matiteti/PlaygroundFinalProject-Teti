from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy




# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


def intro(request):
    return render(request, 'intro.html')

def crear_usuario(request):
    if request.method == 'POST':
        form = Ingresoform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('app1:intro')
    else:
        form = Ingresoform
    return render(request, 'crear_usuario.html', {'form':form})


def menu_inicio(request):
    if request.method == 'POST':
        return redirect('app1:menu')

    return render(request, 'menu_inicio.html')


def menu(request):
    return render(request, 'menu.html')

@login_required
def fruta(request):
    if request.method == 'POST':
        mi_formulario = Frutaform(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            fruta = Fruta(fruta=informacion['fruta'], cantidad=informacion['cantidad'], peso=informacion['peso'])
            fruta.save()
            return redirect('app1:leer_fruta')
        else:
            mi_formulario = Frutaform()
        return render(request, 'fruta.html', {'mi_formulario': mi_formulario})
    
    return render(request, 'fruta.html')


def leer_fruta(request):
    compra_fruta = Fruta.objects.last()  # Obtiene el último registro
    return render(request, 'leer_fruta.html', {'compra_fruta': compra_fruta})


def eliminar_fruta(request, fruta_id):
    fruta = Fruta.objects.get(pk=fruta_id)
    fruta.delete()
    messages.success(request, 'Se ha eliminado la compra.')
    return redirect('app1:fruta')


def editar_fruta(request, fruta_id):
    f = Fruta.objects.get(pk=fruta_id)
    if request.method == "POST":
        mi_formulario = Frutaform(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            f.fruta = informacion['fruta']
            f.peso = informacion['peso']
            f.cantidad = informacion['cantidad']

            f.save()

            return redirect('app1:leer_fruta')
        
    else:
        mi_formulario = Frutaform(initial={'fruta': f.fruta, 'peso': f.peso, 'cantidad': f.cantidad})

    return render(request, "editar_fruta.html", {"mi_formulario": mi_formulario})

@login_required
def panaderia(request):
    if request.method == 'POST':
        pan = request.POST.get('pan')
        cantidad = request.POST.get('cantidad')
        peso = request.POST.get('peso')
        compra = Panaderia(pan=pan, cantidad=cantidad, peso=peso)
        compra.save()
        return redirect('app1:lista_panaderia')

    return render(request, 'panaderia.html')


def lista_panaderia(request):
    compra_pan = Panaderia.objects.last()  # Obtiene el último registro
    return render(request, 'lista_panaderia.html', {'compra_pan': compra_pan})

@login_required
def carniceria(request):
    if request.method == 'POST':
        carne = request.POST.get('carne')
        cantidad = request.POST.get('cantidad')
        peso = request.POST.get('peso')
        compra = Carniceria(carne=carne, cantidad=cantidad, peso=peso)
        compra.save()
        return redirect('app1:lista_carniceria')

    return render(request, 'carniceria.html')


def lista_carniceria(request):
    compra_carne = Carniceria.objects.last()  # Obtiene el último registro
    return render(request, 'lista_carniceria.html', {'compra_carne': compra_carne})


def buscar_fruta_por_id(request):
    elementos = []
    form = BusquedaForm(request.GET)

    if form.is_valid():
        id_busqueda = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if id_busqueda:
            elementos = Fruta.objects.filter(id=id_busqueda)

    return render(request, 'buscar_fruta.html', {'form': form, 'elementos': elementos})


def buscar_carne_por_id(request):
    elementos = []
    form = BusquedaForm(request.GET)

    if form.is_valid():
        id_busqueda = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if id_busqueda:
            elementos = Carniceria.objects.filter(id=id_busqueda)

    return render(request, 'buscar_carne.html', {'form': form, 'elementos': elementos})


def buscar_pan_por_id(request):
    elementos = []
    form = BusquedaForm(request.GET)

    if form.is_valid():
        id_busqueda = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if id_busqueda:
            elementos = Panaderia.objects.filter(id=id_busqueda)

    return render(request, 'buscar_pan.html', {'form': form, 'elementos': elementos})

################################################################################
class FrutaListView(ListView):
    model = Fruta
    context_object_name = "frutas"
    template_name = "app1/fruta_lista.html"


class FrutaDetailView(DetailView):
    model = Fruta
    template_name = "app1/fruta_detalle.html"

class FrutaCreateView(CreateView):
    model = Fruta
    template_name = "app1/fruta_crear.html"
    success_url = reverse_lazy("ListaFruta")
    fields = ["fruta","peso","cantidad"]

class FrutaUpdateView(UpdateView):
    model = Fruta
    template_name = "app1/fruta_editar.html"
    success_url = reverse_lazy("ListaFruta")
    fields = ["fruta","peso","cantidad"]

class FrutaDeleteView(DeleteView):
    model = Fruta
    template_name = "app1/fruta_borrar.html"
    success_url = reverse_lazy("ListaFruta")