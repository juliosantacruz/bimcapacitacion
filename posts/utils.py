from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
# Codigo del Paginator
def info_paginator(posts_list, request, page_request_var, post_per_page):
    queryset = posts_list.order_by('-id')
    paginator = Paginator(queryset, post_per_page)
    
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage: 
        paginated_queryset = paginator.page(paginator.num_pages) 
    return paginated_queryset