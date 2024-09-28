from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Profesor, Mascota
from .forms import ProfesorForm, MascotaForm
from django.shortcuts import render

@login_required
def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'catalogo/listar_profesores.html', {'profesores': profesores})

@login_required
@permission_required('catalogo.add_profesor', raise_exception=True)
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')  
    else:
        form = ProfesorForm()  
    return render(request, 'catalogo/crear_profesor.html', {'form': form})  


@login_required
@permission_required('catalogo.change_profesor', raise_exception=True)
def modificar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'catalogo/modificar_profesor.html', {'form': form})

@login_required
@permission_required('catalogo.delete_profesor', raise_exception=True)
def eliminar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('listar_profesores')
    return render(request, 'catalogo/eliminar_profesor.html', {'profesor': profesor})

@login_required
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'catalogo/listar_mascotas.html', {'mascotas': mascotas})

@login_required
@permission_required('catalogo.add_mascota', raise_exception=True)
def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'catalogo/crear_mascota.html', {'form': form})

@login_required
@permission_required('catalogo.change_mascota', raise_exception=True)
def modificar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'catalogo/modificar_mascota.html', {'form': form})

@login_required
@permission_required('catalogo.delete_mascota', raise_exception=True)
def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('listar_mascotas')
    return render(request, 'catalogo/eliminar_mascota.html', {'mascota': mascota})





def home_view(request):
    return render(request, 'catalogo/home.html')
