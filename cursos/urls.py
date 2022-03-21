from django.urls import path
from .views import *

urlpatterns = [

    #URLS DE CURSOS
    path('', home_cursos, name="cursosHomePage"),
    path('<curso_slug>', page_curso, name="cursoPage"),
    path('<curso_slug>/<clase_slug>', page_clase, name="cursoPage"),


    #URLS DE USUARIOS
    path('signup/', signupuser, name="signupuser"),
    path('logout/', logoutuser, name="logoutuser"),
    path('login/', loginuser, name="loginuser"),
]