from django.shortcuts import render, redirect, get_object_or_404

from apps.estudiante.models import Estudiante, Curso
from .forms import EstudianteForm


def index(request):
    return render(request, 'estudiante/index.html')


def alta_estudiante(request):
    return render(request, 'estudiante/alta_estudiante.html')


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'estudiante/lista_cursos.html', {'cursos': cursos})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'estudiante/confirmacion.html', {'estudiante': form.instance})
    else:
        form = EstudianteForm()
    return render(request, 'estudiante/agregar_estudiante.html', {'form': form})

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.prefetch_related('cursos').all()
    return render(request, 'estudiante/lista_estudiantes.html', {'estudiantes': estudiantes})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiantes = curso.estudiantes.all()  # gracias al related_name en el modelo
    return render(request, 'estudiante/detalle_curso.html', {
        'curso': curso,
        'estudiantes': estudiantes
    })