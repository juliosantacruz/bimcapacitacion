from django.contrib import admin
from django.urls import  path
from .views import *

urlpatterns = [    


    #PUBLICO
    path('<str:slug>', pagina, name='pagina'),

    

]