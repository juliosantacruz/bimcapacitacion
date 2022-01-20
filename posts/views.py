from django.shortcuts import render

from .models import *
# Create your views here.




def home(request):
    featured_post = Post.objects.filter(featured=True)
    context = {
        'featured_post_list':featured_post,
    }
    return render (request, 'home/index.html', context)


def blog(request):
    posts_list = Post.objects.all()

    context = {
        'posts_list':posts_list,
    }
    return render (request, 'home/blog.html', context)