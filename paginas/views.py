from django.shortcuts import render, get_object_or_404
from .models import Pagina
from marketing.models import ContactForm
# Create your views here.



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
        #Aqui se crea el objeto nuevo
        
        contact_form = ContactForm()
        contact_form.nombre = nombre
        contact_form.telefono = telefono
        contact_form.email = email
        contact_form.mensaje = mensaje
        contact_form.save()


    context = {
        'pagina_publicada' : pagina_publicada,
        'pagina' : pagina,
    }
    return render(request, 'home/pagina.html', context)