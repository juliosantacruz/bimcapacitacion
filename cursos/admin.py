from django.contrib import admin
from .models import Student, Tags, Cursos, Clase, Comment
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', ) #visualizar columnas

class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', ) #visualizar columnas

class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', ) #visualizar columnas

class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', ) #visualizar columnas

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', ) #visualizar columnas

admin.site.register(Student, StudentAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Cursos, CursosAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(Comment, CommentAdmin)
