from django.urls import path
from .views import *

urlpatterns = [

    path('', home_cursos, name="cursosHomePage"),
    path('/<slug>', page_curso, name="cursoPage"),



]