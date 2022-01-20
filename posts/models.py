from django.db import models
from django.contrib.auth.models import User


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
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    #comment_count = models.IntegerField(default = 0)
    #view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True )
    thumbnail = models.ImageField(upload_to='media/post/thumbnail')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title