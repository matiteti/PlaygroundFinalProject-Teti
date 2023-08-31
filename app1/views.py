from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import EmailAuthenticationForm, UserEditForm


@login_required(login_url='app1:login')
def index(request):
    return render(request, 'index.html')


def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, f'Se ha creado el usuario {user.get_full_name()}!.')
            return redirect('app1:login')  # Cambia esto a la URL correcta
    else:
        form = UserRegistrationForm()
    return render(request, 'registro.html', {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenido {user.get_full_name()}!.')
            return redirect('app1:index')  # Cambia esto a la URL correcta
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='app1:login')
def user_logout(request):
    logout(request)
    return redirect('app1:index') 

@login_required(login_url='app1:login')
def fruta(request):
    if request.method == 'POST':
        mi_formulario = Frutaform(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            fruta = Fruta(usuario=request.user, fruta=informacion['fruta'], cantidad=informacion['cantidad'], peso=informacion['peso'])
            fruta.save()
            return redirect('app1:leer_fruta')
        else:
            mi_formulario = Frutaform()
        return render(request, 'fruta.html', {'mi_formulario': mi_formulario})
    
    return render(request, 'fruta.html')

@login_required(login_url='app1:login')
def leer_fruta(request):
    compra_fruta = Fruta.objects.last()  # Obtiene el último registro
    user = request.user
    return render(request, 'leer_fruta.html', {'compra_fruta': compra_fruta, 'user': user})

@login_required(login_url='app1:login')
def eliminar_fruta(request, fruta_id):
    fruta = Fruta.objects.get(pk=fruta_id)
    fruta.delete()
    messages.success(request, 'Se ha eliminado la compra.')
    return redirect('app1:fruta')

@login_required(login_url='app1:login')
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

@login_required(login_url='app1:login')
def panaderia(request):
    if request.method == 'POST':
        mi_formulario = Panaderiaform(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            fruta = Panaderia(usuario=request.user, pan=informacion['pan'], cantidad=informacion['cantidad'], peso=informacion['peso'])
            fruta.save()
            return redirect('app1:leer_panaderia')
        else:
            mi_formulario = Panaderiaform()
        return render(request, 'panaderia.html', {'mi_formulario': mi_formulario})
    
    return render(request, 'panaderia.html')

@login_required(login_url='app1:login')
def lista_panaderia(request):
    compra_pan = Panaderia.objects.last()  # Obtiene el último registro
    return render(request, 'lista_panaderia.html', {'compra_pan': compra_pan})

@login_required(login_url='app1:login')
def carniceria(request):
    if request.method == 'POST':
        mi_formulario = Carniceriaform(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            fruta = Carniceria(usuario=request.user, carne=informacion['carne'], cantidad=informacion['cantidad'], peso=informacion['peso'])
            fruta.save()
            return redirect('app1:leer_carne')
        else:
            mi_formulario = Panaderiaform()
        return render(request, 'carniceria.html', {'mi_formulario': mi_formulario})
    
    return render(request, 'carniceria.html')

@login_required(login_url='app1:login')
def lista_carniceria(request):
    compra_carne = Carniceria.objects.last()  # Obtiene el último registro
    return render(request, 'lista_carniceria.html', {'compra_carne': compra_carne})

@login_required(login_url='app1:login')
def buscar_fruta_por_id(request):
    elementos = []
    form = BusquedaForm(request.GET)

    if form.is_valid():
        id_busqueda = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if id_busqueda:
            elementos = Fruta.objects.filter(id=id_busqueda)

    return render(request, 'buscar_fruta.html', {'form': form, 'elementos': elementos})

@login_required(login_url='app1:login')
def buscar_carne_por_id(request):
    elementos = []
    form = BusquedaForm(request.GET)

    if form.is_valid():
        id_busqueda = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if id_busqueda:
            elementos = Carniceria.objects.filter(id=id_busqueda)

    return render(request, 'buscar_carne.html', {'form': form, 'elementos': elementos})

@login_required(login_url='app1:login')
def buscar_pan_por_id(request):
    elementos = []
    form = BusquedaForm(request.GET)

    if form.is_valid():
        id_busqueda = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Curso por nombre
        if id_busqueda:
            elementos = Panaderia.objects.filter(id=id_busqueda)

    return render(request, 'buscar_pan.html', {'form': form, 'elementos': elementos})

@login_required(login_url='app1:login')
def leer_carne(request):
    compra_carne = Carniceria.objects.last()  # Obtiene el último registro
    return render(request, 'leer_carne.html', {'compra_carne': compra_carne})

@login_required(login_url='app1:login')
def eliminar_carne(request, carne_id):
    carne = Carniceria.objects.get(pk=carne_id)
    carne.delete()
    messages.success(request, 'Se ha eliminado la compra.')
    return redirect('app1:carniceria')

@login_required(login_url='app1:login')
def editar_carne(request, carne_id):
    c = Carniceria.objects.get(pk=carne_id)
    if request.method == "POST":
        mi_formulario = Carniceriaform(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            c.carne = informacion['carne']
            c.peso = informacion['peso']
            c.cantidad = informacion['cantidad']

            c.save()

            return redirect('app1:leer_carne')
        
    else:
        mi_formulario = Carniceriaform(initial={'carne': c.carne, 'peso': c.peso, 'cantidad': c.cantidad})

    return render(request, "editar_carne.html", {"mi_formulario": mi_formulario})

@login_required(login_url='app1:login')
def leer_panaderia(request):
    compra_pan = Panaderia.objects.last()  # Obtiene el último registro
    return render(request, 'leer_panaderia.html', {'compra_pan': compra_pan})

@login_required(login_url='app1:login')
def eliminar_pan(request, pan_id):
    pan = Panaderia.objects.get(pk=pan_id)
    pan.delete()
    messages.success(request, 'Se ha eliminado la compra.')
    return redirect('app1:panaderia')

@login_required(login_url='app1:login')
def editar_pan(request, pan_id):
    p = Panaderia.objects.get(pk=pan_id)
    if request.method == "POST":
        mi_formulario = Panaderiaform(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            p.pan = informacion['pan']
            p.peso = informacion['peso']
            p.cantidad = informacion['cantidad']

            p.save()

            return redirect('app1:leer_panaderia')
        
    else:
        mi_formulario = Panaderiaform(initial={'pan': p.pan, 'peso': p.peso, 'cantidad': p.cantidad})

    return render(request, "editar_pan.html", {"mi_formulario": mi_formulario})

@login_required(login_url='app1:login')
def acerca(request):
    return render(request, 'acerca.html')


@login_required(login_url='app1:login')
def editarPerfil(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES , instance=user)
        if form.is_valid():
            new_password = form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
            form.save()
            return redirect('app1:index')  # Cambia esto a la URL del perfil
    else:
        form = UserEditForm(instance=user)
    return render(request, 'editarperfil.html', {'form': form})


@login_required(login_url='app1:login')
def compras(request):
    user = request.user
    compras_fruta = Fruta.objects.filter(usuario=user)
    compras_panaderia = Panaderia.objects.filter(usuario=user)
    compras_carniceria = Carniceria.objects.filter(usuario=user)
    return render(request, 'compras.html', {
        'compras_fruta': compras_fruta,
        'compras_panaderia': compras_panaderia,
        'compras_carniceria': compras_carniceria
    })
