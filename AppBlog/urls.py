from django.urls import path
from AppBlog.views import *

app_name = 'AppBlog'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('reglas/', reglas, name='reglas'),
    path('lotr', lotr, name='lotr'),
    path('mistborn/', mistborn, name='mistborn'),
    path('narnia/', narnia, name='narnia'),
    path('got', got, name='got'),
    path('mensajes', mensajes, name='mensajes'),
    path('posts/', posts, name='posts'),
]