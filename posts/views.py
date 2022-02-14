from datetime import time
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from .models import *
from .utils import info_paginator
from marketing.models import Signup

from django.views.generic import (TemplateView)
# Create your views here.


class error_404(TemplateView):
    template_name = "home/error404.html"


#Funcion para hacer busquedas
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context={
        'queryset':queryset
    }
    return render(request, 'home/search_results.html', context)


def home(request):
    
    featured_post = Post.objects.filter(featured=True).order_by('?')[:4]


    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()


    context = {
        'featured_post_list':featured_post,
    }
    return render (request, 'home/index.html', context)


def descargas(request):
    nombre_url = request.resolver_match.url_name
    posts_list = Post.objects.filter(category__title='descargas')


    # Codigo del Paginator
    page_request_var = 'page'
    post_per_page = 6
    paginated_queryset = info_paginator(posts_list, request, page_request_var, post_per_page)
    

    context = {
        'posts_list':paginated_queryset,
        'page_request_var':page_request_var,
        'nombre_url':nombre_url,
        
    }
    return render (request, 'home/blog.html', context)


def blog(request):
    nombre_url = request.resolver_match.url_name
    
    posts_list = Post.objects.all()


    # Codigo del Paginator
    page_request_var = 'page'
    post_per_page = 6
    paginated_queryset = info_paginator(posts_list, request, page_request_var, post_per_page)
    

    context = {
        'posts_list':paginated_queryset,
        'page_request_var':page_request_var,
        'nombre_url':nombre_url,
        
    }
    return render (request, 'home/blog.html', context)


def post(request, category, slug):
    post = get_object_or_404(Post, slug=slug)
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    

    


    context = {
        'post':post,
        'next_post':next_post,
        'prev_post':prev_post,
    }
    return render (request, 'home/post.html', context)




    