from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso
from django.core import serializers
from AppCoder.forms import CursoFormulario
 
def cursos(request):
 
      if request.method == "POST":
 
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"], numero_dia=informacion["numero_dia"])
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


#Buscar
def busquedaCamada(request):
    return render(request, "AppCoder/busquedaComision.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request,"AppCoder/resultadosBusqueda.html",{"cursos":cursos,"camada":camada})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

# Create your views here.
def inicio(request):
    return render(request,'AppCoder/inicio.html')    

def profesores(request):
    return HttpResponse('Vista de profesores')    

def cursosapi(request):
    cursos_todos = Curso.objects.all()
    return HttpResponse(serializers.serialize('json',cursos_todos)) 

    