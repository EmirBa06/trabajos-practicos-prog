from django.urls import path
from . import views

app_name = 'estudiante'

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.alta_estudiante, name='alta_estudiante'),
    path('listar_cursos', views.listar_cursos, name='listar_cursos'),
    path('agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('listar', views.listar_estudiantes, name='listar_estudiantes')
]