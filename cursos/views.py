from django.shortcuts import render, get_object_or_404

from cursos.models import Cursos
from .models import *
# Create your views here.

def home_cursos(request ): #Aqui van todos los cursos
    cursos_list = Cursos.objects.all()

    context = {
    'cursos_list':cursos_list,
    }

    return render (request, 'cursos/homeCursos.html', context)


def page_curso(request, curso_slug ): #Pagina principal del curso 
    curso = get_object_or_404(Cursos, curso_slug=curso_slug)
    clases = Clase.objects.all()
    


    context = {
    'curso':curso,
    'clases':clases,
    
    }
    return render (request, 'cursos/curso.html', context)


def page_clase(request, curso_slug, clase_slug ): #Pagina principal del curso 
    
    


    context = {
    
    
    }
    return render (request, 'cursos/clase.html', context)