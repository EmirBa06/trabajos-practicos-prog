from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre_estudiante',
            'apellido_estudiante',
            'edad_estudiante',
            'curso_estudiante',
            'nota_curso_estudiante',
            'cursos'
        ]
