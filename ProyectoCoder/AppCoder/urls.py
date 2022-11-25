from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio,name='Inicio'),
    path("cursos/", views.cursos,name='Cursos'),
    path("cursosApi/", views.cursosapi),
    path("profesores/", views.profesores),
    #path("cursoFormulario/", views.cursoFormulario),
    path("busquedaCamada/", views.busquedaCamada),
    path("buscar/", views.buscar)
]
