from django.db import models

class Curso(models.Model):
    nombre_curso = models.TextField(max_length=250, unique=True)
    cantidad_horas_curso = models.TextField(unique=True)

    def __str__(self):
        return f'Nombre Curso:{self.nombre_curso}, Cantidad de horas:{self.cantidad_horas_curso}'
    

class Estudiante(models.Model):
    nombre_estudiante = models.TextField(max_length=250, unique=True)
    apellido_estudiante = models.TextField(max_length=250, unique=True)
    edad_estudiante = models.IntegerField(unique=True)
    nota_curso_estudiante = models.IntegerField(blank=True, null=True)
    curso_estudiante = models.TextField(blank=True)

    cursos = models.ManyToManyField(Curso, related_name='estudiantes')

    def __str__(self):
        return f'Nombre: {self.nombre_estudiante}, Apellido: {self.apellido_estudiante}, Edad: {self.edad_estudiante}, Nota: {self.nota_curso_estudiante}, Curso: {self.curso_estudiante}'



# Create your models here.


