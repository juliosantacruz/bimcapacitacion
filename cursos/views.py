from django.shortcuts import render, get_object_or_404

from cursos.models import Cursos
from .models import *
# Create your views here.

def home_cursos(request ):
    cursos_list = Cursos.objects.all()

    context = {
    'cursos_list':cursos_list,
    }

    return render (request, 'cursos/homeCursos.html', context)


def page_curso(request, slug ):
    curso = get_object_or_404(Cursos, slug=slug)



    context = {
    'curso':curso,
    
    }
    return render (request, 'cursos/homeCursos.html', context)