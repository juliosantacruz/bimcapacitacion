from email.policy import default
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True  )
    profile_picture =  models.ImageField(upload_to='media/author')
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title


class Post(models.Model):
    slug = models.SlugField(unique=True,verbose_name="url del sitio"  )
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = RichTextUploadingField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #comment_count = models.IntegerField(default = 0)
    #view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True )
    thumbnail = models.ImageField(upload_to='media/post/thumbnail')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'categoria' )
    tags = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title