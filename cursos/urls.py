from django.urls import path
from .views import *

urlpatterns = [

    path('', home_cursos, name="cursosHomePage"),
    path('<curso_slug>', page_curso, name="cursoPage"),
    path('<curso_slug>/<clase_slug>', page_clase, name="cursoPage"),



]