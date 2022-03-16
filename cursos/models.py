from django.db import models
from posts.models import Author
# Create your models here.
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='media/cursos/users', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Tags(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title


class Cursos(models.Model):
    slug = models.SlugField(unique=True,verbose_name="url del sitio"  )
    title = models.CharField(max_length=150)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='media/cursos/thumbnail')
    
    def __str__(self):
        return self.title


class Clase(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,verbose_name="url del sitio"  )
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    tags= models.ManyToManyField(Tags)
    for_free = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True )
    thumbnail = models.ImageField(upload_to='media/cursos/thumbnail')
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.CharField(max_length=250)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, blank=True, null=True)