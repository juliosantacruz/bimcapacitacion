from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from cursos.models import Cursos
from .models import *
from .forms import CreateUserForm

# Create your views here.

# USERS
#USER ONLY

def signupuser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            if User.objects.filter(email = request.POST['email']).exists():
                error = 'Tu correo ya fue registrado, intenta con otro'
                context = {
                    'error':error,
                    'form': form,
                }
                return render(request, 'cursos/signupuser.html', context)
            else:
                try: 
                    user = User.objects.create_user(
                        request.POST['username'], 
                        first_name=request.POST['first_name'], 
                        last_name=request.POST['last_name'], 
                        email=request.POST['email'] , 
                        password=request.POST['password1'])
                    perfil = Student.objects.create(
                        user = User.objects.all().last(),
                        email = request.POST['email'] # <--- aqui agregamos el email para que se unique
                        #profile_picture=request.FILES['img'] <--- De momento no se requiere foto
                        )

                    user.save()
                    perfil.save()
                    login(request, user)
                    return redirect('cursosHomePage')
                except IntegrityError:
                    error = 'Tu nombre de usuario fue tomado, intenta con otro'
                    context = {
                        'error':error,
                        'form': form,
                    }
                return render(request, 'cursos/signupuser.html', context)
        else:
            error = 'Error al escribir tu contrasena'
            context={'error':error,
                    'form': form,}
            return render(request, 'cursos/signupuser.html', context)
    else:
        context={
            'form': form
        }
        return render(request, 'cursos/signupuser.html', context)


#USER ONLY
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('cursosHomePage')


def loginuser(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['Password'])
        if user is None:
            return render(request, 'cursos/loginuser.html', {'form': AuthenticationForm() , 'error': 'User or password did not match'})
        else:
            login(request, user)
            return redirect('cursosHomePage')
    else:
        return render(request, 'cursos/loginuser.html',  {'form': AuthenticationForm()})



# PAGINAS
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
    clase = get_object_or_404(Clase, clase_slug=clase_slug)
    
    


    context = {
    'clase' : clase,
    
    }
    return render (request, 'cursos/clase.html', context)