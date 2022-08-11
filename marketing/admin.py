from django.contrib import admin
from .models import *
# Register your models here.

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'mensaje' ,'creado') #visualizar columnas

class SignupAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'timestamp') #visualizar columnas



admin.site.register(Signup, SignupAdmin)
admin.site.register(ContactForm, ContactFormAdmin)