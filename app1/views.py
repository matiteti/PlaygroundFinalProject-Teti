from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib import messages
from .forms import *


# Create your views here.

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


def fruta(request):
    if request.method == 'POST':
        fruta = request.POST.get('fruta')
        cantidad = request.POST.get('cantidad')
        peso = request.POST.get('peso')
        compra_fruta = Fruta(fruta=fruta, cantidad=cantidad, peso=peso)
        compra_fruta.save()
        return redirect('app1:lista_fruta')

    return render(request, 'fruta.html')

def lista_fruta(request):
    compra_fruta = Fruta.objects.last()  # Obtiene el último registro
    return render(request, 'lista_fruta.html', {'compra_fruta': compra_fruta})


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

