#from email import message
from urllib import response
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pagina
from marketing.models import ContactForm
from django.conf import settings
from posts.views import *
# Create your views here.

#Utilizamos estas librerias para recaptcha
import json
import urllib
from django.contrib import messages


def pagina(request, slug):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    pagina = get_object_or_404(Pagina, slug=slug)



    #CONTACT FORM
    if request.method == 'POST':
        #Aqui ordenamos la informacion del POST
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        
        #Aqui verificamos reCaptcha
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        
        #Aqui se crea el objeto nuevo
        if result['success']: #esta es la condicion del recaptcha correcto
            contact_form = ContactForm()
            contact_form.nombre = nombre
            contact_form.telefono = telefono
            contact_form.email = email
            contact_form.mensaje = mensaje
            contact_form.save()
            messages.success(request, 'done')
        else: 
            messages.error(request, 'Invalid reCAPTCHA. Please try again')
        return redirect('homepage')

    context = {
        'pagina_publicada' : pagina_publicada,
        'pagina' : pagina,
    }
    return render(request, 'home/pagina.html', context)