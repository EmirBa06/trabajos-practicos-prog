from django.contrib import admin
from .models import Curso, Estudiante # Es mejor usar la importación relativa .models

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # 👇 Campos del modelo Curso
    list_display = ['nombre_curso', 'cantidad_horas_curso'] 
    search_fields = ['nombre_curso']

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    # 👇 Campos del modelo Estudiante
    list_display = ['nombre_estudiante', 'apellido_estudiante', 'edad_estudiante', 'nota_curso_estudiante', 'curso_estudiante']
    search_fields = ['nombre_estudiante', 'apellido_estudiante']