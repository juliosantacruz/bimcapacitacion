from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name="homepage"),
    path('blog', blog, name='blogpage'),
    path('search', search, name='search'),
    path('<category>/<slug>', post, name='postpage'),


]